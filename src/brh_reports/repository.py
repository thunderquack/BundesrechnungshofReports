from __future__ import annotations

import json
from pathlib import Path

from brh_reports.models import DownloadedReport


def ensure_directories(*paths: Path) -> None:
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)


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
