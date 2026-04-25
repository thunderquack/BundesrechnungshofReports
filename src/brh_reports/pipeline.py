from __future__ import annotations

from brh_reports.config import get_settings
from brh_reports.crawler import discover_report_candidates
from brh_reports.downloader import download_report
from brh_reports.repository import ensure_directories, save_markdown, save_metadata


def discover_pipeline() -> list:
    settings = get_settings()
    candidates = list(discover_report_candidates(settings))
    print(f"Discovered {len(candidates)} report candidates.")
    return candidates


def download_pipeline() -> int:
    settings = get_settings()
    ensure_directories(settings.temp_dir)

    candidates = list(discover_report_candidates(settings))
    print(f"Discovered {len(candidates)} report candidates.")
    for index, candidate in enumerate(candidates, start=1):
        downloaded = download_report(candidate, settings.temp_dir)
        print(f"[{index}/{len(candidates)}] Downloaded {downloaded.pdf_path}")

    return 0


def run_pipeline() -> int:
    return download_pipeline()
