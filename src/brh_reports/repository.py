from __future__ import annotations

import json
import re
from datetime import date, datetime
from pathlib import Path

from brh_reports.identity import build_report_identity_value, build_report_key
from brh_reports.models import DownloadedReport, ReportCandidate

MAX_MARKDOWN_SLUG_LENGTH = 80


def ensure_directories(*paths: Path) -> None:
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "report"


def _build_markdown_path(report: ReportCandidate, markdown_dir: Path) -> Path:
    year = "unknown-year"
    date_prefix = "unknown-date"
    if report.published_on and len(report.published_on.split(".")) == 3:
        day, month, year = report.published_on.split(".")
        date_prefix = f"{year}-{month}-{day}"
    slug = _slugify(report.title)
    if len(slug) > MAX_MARKDOWN_SLUG_LENGTH:
        slug = f"{slug[:MAX_MARKDOWN_SLUG_LENGTH]}-{build_report_key(report)[:12]}"
    return markdown_dir / year / f"{date_prefix}-{slug}.md"


def _normalize_manifest_entries(payload: dict) -> list[dict]:
    entries = payload.get("reports", [])
    if not isinstance(entries, list):
        return []
    return [entry for entry in entries if isinstance(entry, dict)]


def load_processed_report_keys(manifest_path: Path) -> set[str]:
    if not manifest_path.exists():
        return set()

    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = _normalize_manifest_entries(payload)
    return {entry["report_key"] for entry in entries if "report_key" in entry}


def load_processed_reports(manifest_path: Path) -> dict[str, dict]:
    if not manifest_path.exists():
        return {}

    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = _normalize_manifest_entries(payload)
    processed: dict[str, dict] = {}
    for entry in entries:
        report_key = entry.get("report_key")
        if isinstance(report_key, str):
            processed[report_key] = entry
    return processed


def _parse_report_date(value: str | None) -> date:
    if not value:
        return date.min

    for date_format in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, date_format).date()
        except ValueError:
            continue
    return date.min


def save_processed_reports(manifest_path: Path, processed_reports: dict[str, dict]) -> Path:
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "reports": sorted(
            processed_reports.values(),
            key=lambda entry: (
                _parse_report_date(entry.get("published_on")),
                entry.get("title") or "",
            ),
            reverse=True,
        )
    }
    manifest_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return manifest_path


def save_markdown(report: ReportCandidate, markdown: str, target_dir: Path) -> Path:
    """Persist converted Markdown for a report."""
    output_path = _build_markdown_path(report, target_dir)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
    return output_path


def build_processed_report_entry(report: ReportCandidate, markdown_path: Path) -> dict:
    return {
        "report_key": build_report_key(report),
        "identity_value": build_report_identity_value(report),
        "title": report.title,
        "published_on": report.published_on,
        "pdf_url": report.pdf_url,
        "summary": report.summary,
        "markdown_path": markdown_path.as_posix(),
    }


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
