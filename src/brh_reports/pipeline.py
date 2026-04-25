from __future__ import annotations

from brh_reports.config import get_settings
from brh_reports.converter import convert_pdf_to_markdown
from brh_reports.crawler import discover_report_candidates
from brh_reports.downloader import download_report
from brh_reports.repository import ensure_directories, save_markdown, save_metadata


def run_pipeline() -> int:
    settings = get_settings()
    ensure_directories(settings.raw_dir, settings.markdown_dir, settings.metadata_dir)

    candidates = list(discover_report_candidates())
    if not candidates:
        print("No report candidates discovered yet. Crawler is still a placeholder.")
        return 0

    for candidate in candidates:
        downloaded = download_report(candidate, settings.raw_dir)
        markdown = convert_pdf_to_markdown(settings.raw_dir / downloaded.pdf_path)
        save_markdown(downloaded, markdown, settings.markdown_dir)
        save_metadata(downloaded, settings.metadata_dir)

    return 0
