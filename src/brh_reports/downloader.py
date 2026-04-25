from __future__ import annotations

from pathlib import Path

from playwright.sync_api import APIRequestContext, BrowserContext, sync_playwright

from brh_reports.identity import build_report_key
from brh_reports.models import DownloadedReport, ReportCandidate


def _build_file_name(candidate: ReportCandidate) -> str:
    return f"{build_report_key(candidate)}.pdf"


def download_report(
    candidate: ReportCandidate,
    target_dir: Path,
    request_context: APIRequestContext | None = None,
    browser_context: BrowserContext | None = None,
) -> DownloadedReport:
    """Download a single report PDF.

    Download the PDF into a temporary directory using Playwright's request client.
    """
    if not candidate.pdf_url:
        raise ValueError(f"Candidate '{candidate.title}' has no PDF URL.")

    target_dir.mkdir(parents=True, exist_ok=True)
    file_name = _build_file_name(candidate)
    output_path = target_dir / file_name

    if browser_context is not None:
        page = browser_context.new_page()
        try:
            response = page.goto(candidate.pdf_url, wait_until="domcontentloaded")
            if response is None or not response.ok:
                status = "no-response" if response is None else response.status
                raise RuntimeError(
                    f"Failed to download PDF: {candidate.pdf_url} ({status})"
                )
            output_path.write_bytes(response.body())
        finally:
            page.close()
    elif request_context is not None:
        response = request_context.get(candidate.pdf_url)
        if not response.ok:
            raise RuntimeError(
                f"Failed to download PDF: {candidate.pdf_url} ({response.status})"
            )
        output_path.write_bytes(response.body())
    else:
        with sync_playwright() as playwright:
            request_context = playwright.request.new_context(extra_http_headers={"User-Agent": "Mozilla/5.0"})
            try:
                response = request_context.get(candidate.pdf_url)
                if not response.ok:
                    raise RuntimeError(
                        f"Failed to download PDF: {candidate.pdf_url} ({response.status})"
                    )
                output_path.write_bytes(response.body())
            finally:
                request_context.dispose()

    return DownloadedReport(
        title=candidate.title,
        source_url=candidate.pdf_url,
        pdf_path=file_name,
    )
