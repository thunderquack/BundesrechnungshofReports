from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright

from brh_reports.models import DownloadedReport, ReportCandidate


def _build_file_name(candidate: ReportCandidate) -> str:
    if candidate.pdf_url:
        file_name = Path(urlparse(candidate.pdf_url).path).name
        if file_name:
            return file_name
    fallback = "".join(ch if ch.isalnum() else "-" for ch in candidate.title.lower()).strip("-")
    return f"{fallback or 'report'}.pdf"


def download_report(candidate: ReportCandidate, target_dir: Path) -> DownloadedReport:
    """Download a single report PDF.

    Download the PDF into a temporary directory using Playwright's request client.
    """
    if not candidate.pdf_url:
        raise ValueError(f"Candidate '{candidate.title}' has no PDF URL.")

    target_dir.mkdir(parents=True, exist_ok=True)
    file_name = _build_file_name(candidate)
    output_path = target_dir / file_name

    with sync_playwright() as playwright:
        request_context = playwright.request.new_context(extra_http_headers={"User-Agent": "Mozilla/5.0"})
        try:
            response = request_context.get(candidate.pdf_url)
            response.raise_for_status()
            output_path.write_bytes(response.body())
        finally:
            request_context.dispose()

    return DownloadedReport(
        title=candidate.title,
        source_url=candidate.pdf_url,
        pdf_path=file_name,
    )
