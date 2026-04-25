from __future__ import annotations

from pathlib import Path

from playwright.sync_api import APIRequestContext, sync_playwright

from brh_reports.identity import build_report_key
from brh_reports.models import DownloadedReport, ReportCandidate


def _build_file_name(candidate: ReportCandidate) -> str:
    return f"{build_report_key(candidate)}.pdf"


def download_report(
    candidate: ReportCandidate,
    target_dir: Path,
    request_context: APIRequestContext | None = None,
) -> DownloadedReport:
    """Download a single report PDF.

    Download the PDF into a temporary directory using Playwright's request client.
    """
    if not candidate.pdf_url:
        raise ValueError(f"Candidate '{candidate.title}' has no PDF URL.")

    target_dir.mkdir(parents=True, exist_ok=True)
    file_name = _build_file_name(candidate)
    output_path = target_dir / file_name

    if request_context is not None:
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
