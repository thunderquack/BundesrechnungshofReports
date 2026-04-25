from __future__ import annotations

import re
from collections.abc import Iterable
from urllib.parse import urlencode, urljoin

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

from brh_reports.config import Settings, get_settings
from brh_reports.models import ReportCandidate

RESULT_COUNT_RE = re.compile(r"von\s+([\d.]+)\s+Ergebnissen")
DATE_RE = re.compile(r"\b\d{2}\.\d{2}\.\d{4}\b")


def _normalize_whitespace(text: str) -> str:
    return " ".join(text.split())


def _extract_total_results(soup: BeautifulSoup) -> int | None:
    result_count = soup.select_one("#resultCount")
    if result_count is None:
        return None

    match = RESULT_COUNT_RE.search(result_count.get_text(" ", strip=True))
    if match is None:
        return None

    return int(match.group(1).replace(".", ""))


def _extract_title(title_node: BeautifulSoup) -> str:
    title_soup = BeautifulSoup(str(title_node), "html.parser")
    for extra in title_soup.select("span.aural, span.category"):
        extra.decompose()
    return _normalize_whitespace(title_soup.get_text(" ", strip=True))


def _parse_search_page(html: str, current_url: str, base_url: str) -> tuple[list[ReportCandidate], str | None, int | None]:
    soup = BeautifulSoup(html, "html.parser")
    candidates: list[ReportCandidate] = []

    for teaser in soup.select("section.searchresult div.teaser.type-1.Report"):
        title_node = teaser.select_one("h3.withHeader")
        pdf_link = teaser.select_one("a.c-button[href]")
        if title_node is None or pdf_link is None:
            continue

        title = _extract_title(title_node)
        pdf_url = urljoin(base_url, pdf_link["href"])
        summary_node = teaser.select_one("p")
        summary = None
        if summary_node is not None:
            summary = _normalize_whitespace(summary_node.get_text(" ", strip=True)) or None

        category_node = title_node.select_one("span.category")
        published_on = None
        if category_node is not None:
            category_text = _normalize_whitespace(category_node.get_text(" ", strip=True))
            match = DATE_RE.search(category_text)
            if match is not None:
                published_on = match.group(0)

        candidates.append(
            ReportCandidate(
                title=title,
                detail_url=current_url,
                pdf_url=pdf_url,
                summary=summary,
                published_on=published_on,
            )
        )

    next_link = soup.select_one("nav.navIndex a.forward.button[href]")
    next_url = None if next_link is None else urljoin(base_url, next_link["href"])
    total_results = _extract_total_results(soup)
    return candidates, next_url, total_results


def discover_report_candidates(settings: Settings | None = None) -> Iterable[ReportCandidate]:
    """Discover all report candidates from the Bundesrechnungshof search page."""
    settings = settings or get_settings()
    start_url = f"{settings.search_url}?{urlencode({'resultsPerPage': settings.results_per_page})}"
    discovered: list[ReportCandidate] = []
    seen_pdf_urls: set[str] = set()
    visited_pages: set[str] = set()
    next_url: str | None = start_url

    with sync_playwright() as playwright:
        request_context = playwright.request.new_context(
            base_url=settings.base_url,
            extra_http_headers={"User-Agent": settings.user_agent},
        )
        try:
            while next_url and next_url not in visited_pages:
                visited_pages.add(next_url)
                response = request_context.get(next_url)
                if not response.ok:
                    raise RuntimeError(f"Failed to fetch search page: {next_url} ({response.status})")

                page_candidates, following_url, total_results = _parse_search_page(
                    response.text(),
                    current_url=next_url,
                    base_url=settings.base_url,
                )
                for candidate in page_candidates:
                    if candidate.pdf_url is None or candidate.pdf_url in seen_pdf_urls:
                        continue
                    seen_pdf_urls.add(candidate.pdf_url)
                    discovered.append(candidate)

                next_url = following_url
                if total_results is not None and len(discovered) >= total_results:
                    break
        finally:
            request_context.dispose()

    return discovered
