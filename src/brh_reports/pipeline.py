from __future__ import annotations

from brh_reports.config import get_settings
from brh_reports.crawler import discover_report_candidates
from brh_reports.downloader import download_report
from brh_reports.identity import build_report_key
from brh_reports.repository import ensure_directories, load_processed_report_keys, save_processed_reports


def discover_pipeline() -> list:
    settings = get_settings()
    candidates = list(discover_report_candidates(settings))
    print(f"Discovered {len(candidates)} report candidates.")
    return candidates


def download_pipeline() -> int:
    settings = get_settings()
    ensure_directories(settings.temp_dir, settings.state_dir)

    candidates = list(discover_report_candidates(settings))
    print(f"Discovered {len(candidates)} report candidates.")
    processed_keys = load_processed_report_keys(settings.manifest_path)
    new_candidates = [candidate for candidate in candidates if build_report_key(candidate) not in processed_keys]
    print(f"New report candidates: {len(new_candidates)}")

    for index, candidate in enumerate(new_candidates, start=1):
        downloaded = download_report(candidate, settings.temp_dir)
        print(f"[{index}/{len(new_candidates)}] Downloaded {downloaded.pdf_path}")

    save_processed_reports(settings.manifest_path, candidates)

    return 0


def run_pipeline() -> int:
    return download_pipeline()
