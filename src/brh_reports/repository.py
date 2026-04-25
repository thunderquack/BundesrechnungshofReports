from __future__ import annotations

import json
from pathlib import Path

from brh_reports.identity import build_report_identity_value, build_report_key
from brh_reports.models import DownloadedReport, ReportCandidate


def ensure_directories(*paths: Path) -> None:
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)


def load_processed_report_keys(manifest_path: Path) -> set[str]:
    if not manifest_path.exists():
        return set()

    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = payload.get("reports", [])
    return {entry["report_key"] for entry in entries if "report_key" in entry}


def save_processed_reports(manifest_path: Path, reports: list[ReportCandidate]) -> Path:
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "reports": [
            {
                "report_key": build_report_key(report),
                "identity_value": build_report_identity_value(report),
                "title": report.title,
                "published_on": report.published_on,
                "pdf_url": report.pdf_url,
                "detail_url": report.detail_url,
                "summary": report.summary,
            }
            for report in reports
        ]
    }
    manifest_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return manifest_path


def save_markdown(report: DownloadedReport, markdown: str, target_dir: Path) -> Path:
    """Persist converted Markdown for a report."""
    output_path = target_dir / "placeholder.md"
    output_path.write_text(markdown, encoding="utf-8")
    return output_path


def save_metadata(report: DownloadedReport, target_dir: Path) -> Path:
    """Persist basic metadata for a report."""
    output_path = target_dir / "placeholder.json"
    payload = {
        "title": report.title,
        "source_url": report.source_url,
        "pdf_path": report.pdf_path,
    }
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return output_path
