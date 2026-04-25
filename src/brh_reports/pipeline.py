from __future__ import annotations

import time
from pathlib import Path

from playwright.sync_api import sync_playwright
from tqdm import tqdm

from brh_reports.config import get_settings
from brh_reports.converter import convert_pdf_to_markdown
from brh_reports.crawler import discover_report_candidates
from brh_reports.downloader import download_report
from brh_reports.identity import build_report_key
from brh_reports.repository import (
    build_processed_report_entry,
    ensure_directories,
    load_processed_report_keys,
    load_processed_reports,
    save_markdown,
    save_processed_reports,
)


def discover_pipeline() -> list:
    settings = get_settings()
    candidates = list(discover_report_candidates(settings))
    print(f"Discovered {len(candidates)} report candidates.")
    return candidates


def download_pipeline() -> int:
    return run_pipeline()


def _cleanup_file(path: Path) -> None:
    for _ in range(5):
        try:
            path.unlink(missing_ok=True)
            return
        except PermissionError:
            time.sleep(0.2)


def run_pipeline() -> int:
    settings = get_settings()
    ensure_directories(settings.temp_dir, settings.state_dir, settings.markdown_dir)

    candidates = list(discover_report_candidates(settings))
    print(f"Discovered {len(candidates)} report candidates.")
    processed_keys = load_processed_report_keys(settings.manifest_path)
    processed_reports = load_processed_reports(settings.manifest_path)
    new_candidates = [candidate for candidate in candidates if build_report_key(candidate) not in processed_keys]
    print(f"New report candidates: {len(new_candidates)}")

    if not new_candidates:
        return 0

    with sync_playwright() as playwright:
        request_context = playwright.request.new_context(extra_http_headers={"User-Agent": settings.user_agent})
        try:
            with tqdm(new_candidates, desc="Processing new reports", unit="report") as progress:
                for candidate in progress:
                    downloaded = download_report(candidate, settings.temp_dir, request_context=request_context)
                    pdf_path = settings.temp_dir / downloaded.pdf_path
                    try:
                        markdown = convert_pdf_to_markdown(pdf_path)
                        markdown_path = save_markdown(candidate, markdown, settings.markdown_dir)
                        processed_reports[build_report_key(candidate)] = build_processed_report_entry(
                            candidate,
                            markdown_path,
                        )
                        save_processed_reports(settings.manifest_path, processed_reports)
                        progress.set_postfix(saved=markdown_path.name)
                    finally:
                        _cleanup_file(pdf_path)
        finally:
            request_context.dispose()

    return 0
