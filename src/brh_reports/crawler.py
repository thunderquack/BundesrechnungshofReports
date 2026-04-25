from __future__ import annotations

import re
import time
from collections.abc import Iterable
from collections.abc import Callable
from html import unescape
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit

from bs4 import BeautifulSoup
from playwright.sync_api import Error, sync_playwright

from brh_reports.config import Settings, get_settings
from brh_reports.models import ReportCandidate

RESULT_COUNT_RE = re.compile(r"von\s+([\d.]+)\s+Ergebnissen")
DATE_RE = re.compile(r"\b\d{2}\.\d{2}\.\d{4}\b")
CURRENT_PAGE_RE = re.compile(r"Sie sind hier: Seite\s*(\d+)")
FORWARD_LINK_RE = re.compile(r'href="([^"]+)"\s+title="Seite\s+2"\s+class="forward button"')
TRAILING_NUMBER_RE = re.compile(r"^(.*?)(\d+)$")


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


def _extract_current_page(html: str, current_url: str) -> int:
    match = CURRENT_PAGE_RE.search(html)
    if match is not None:
        return int(match.group(1))

    return 1


def _extract_page_url_builder(first_page_html: str, settings: Settings) -> Callable[[int], str]:
    match = FORWARD_LINK_RE.search(first_page_html)
    if match is None:
        return settings.page_url

    second_page_url = urljoin(settings.base_url, unescape(match.group(1)))
    parsed = urlsplit(second_page_url)
    query_items = parse_qsl(parsed.query, keep_blank_values=True)

    page_parameter_index: int | None = None
    page_parameter_prefix: str | None = None
    for index, (key, value) in enumerate(query_items):
        value_match = TRAILING_NUMBER_RE.match(value)
        if value_match is None:
            continue
        prefix, trailing_number = value_match.groups()
        if trailing_number != "2":
            continue
        page_parameter_index = index
        page_parameter_prefix = prefix
        break

    if page_parameter_index is None or page_parameter_prefix is None:
        return settings.page_url

    def build_page_url(page_number: int) -> str:
        if page_number <= 1:
            return settings.page_url(1)
        updated_query_items = list(query_items)
        key, _ = updated_query_items[page_parameter_index]
        updated_query_items[page_parameter_index] = (
            key,
            f"{page_parameter_prefix}{page_number}",
        )
        return urlunsplit(
            (
                parsed.scheme,
                parsed.netloc,
                parsed.path,
                urlencode(updated_query_items),
                parsed.fragment,
            )
        )

    return build_page_url


def _parse_search_page(html: str, current_url: str, base_url: str) -> tuple[list[ReportCandidate], str | None, int | None]:
    soup = BeautifulSoup(html, "html.parser")
    candidates: list[ReportCandidate] = []

    for teaser in soup.select("section.searchresult div.teaser.type-1.Report"):
        title_node = teaser.select_one("h3.withHeader")
        pdf_link = teaser.select_one('a.c-button[href*=".pdf"]')
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

    current_page = _extract_current_page(html, current_url)
    next_url = None if current_page < 1 else str(current_page + 1)
    total_results = _extract_total_results(soup)
    return candidates, next_url, total_results


def _fetch_search_page(playwright, url: str, settings: Settings, retries: int = 3) -> str:
    last_error: Exception | None = None
    for attempt in range(retries):
        request_context = playwright.request.new_context(
            base_url=settings.base_url,
            extra_http_headers={"User-Agent": settings.user_agent},
        )
        try:
            response = request_context.get(url)
            if not response.ok:
                if response.status == 429 or response.status >= 500:
                    time.sleep(settings.request_delay_seconds * (attempt + 2))
                    continue
                raise RuntimeError(f"Failed to fetch search page: {url} ({response.status})")
            return response.text()
        except Error as exc:
            last_error = exc
            time.sleep(settings.request_delay_seconds * (attempt + 2))
        finally:
            request_context.dispose()

    raise RuntimeError(f"Failed to fetch search page after {retries} attempts: {url}") from last_error


def discover_report_candidates(settings: Settings | None = None) -> Iterable[ReportCandidate]:
    """Discover all report candidates from the Bundesrechnungshof search page."""
    settings = settings or get_settings()
    discovered: list[ReportCandidate] = []
    seen_pdf_urls: set[str] = set()

    with sync_playwright() as playwright:
        first_url = settings.page_url(1)
        first_html = _fetch_search_page(playwright, first_url, settings)
        page_url_builder = _extract_page_url_builder(first_html, settings)
        first_candidates, _, total_results = _parse_search_page(
            first_html,
            current_url=first_url,
            base_url=settings.base_url,
        )
        for candidate in first_candidates:
            if candidate.pdf_url is None or candidate.pdf_url in seen_pdf_urls:
                continue
            seen_pdf_urls.add(candidate.pdf_url)
            discovered.append(candidate)

        if total_results is None:
            return discovered

        for page_number in range(2, settings.total_pages(total_results) + 1):
            page_url = page_url_builder(page_number)
            html = _fetch_search_page(playwright, page_url, settings)
            page_candidates, _, _ = _parse_search_page(
                html,
                current_url=page_url,
                base_url=settings.base_url,
            )
            for candidate in page_candidates:
                if candidate.pdf_url is None or candidate.pdf_url in seen_pdf_urls:
                    continue
                seen_pdf_urls.add(candidate.pdf_url)
                discovered.append(candidate)
            time.sleep(settings.request_delay_seconds)

    return discovered
