import json
from pathlib import Path

from brh_reports.models import ReportCandidate
from brh_reports.repository import load_processed_report_keys, save_processed_reports


def test_manifest_roundtrip(tmp_path: Path) -> None:
    manifest_path = tmp_path / "processed_reports.json"
    reports = [
        ReportCandidate(
            title="Example Report",
            detail_url="https://example.com/detail",
            pdf_url="https://example.com/report.pdf",
            published_on="25.04.2026",
        )
    ]

    save_processed_reports(manifest_path, reports)

    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert len(payload["reports"]) == 1
    assert payload["reports"][0]["title"] == "Example Report"
    assert load_processed_report_keys(manifest_path) == {payload["reports"][0]["report_key"]}
