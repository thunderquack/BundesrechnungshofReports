import json
from pathlib import Path

from brh_reports.identity import build_report_key
from brh_reports.models import ReportCandidate
from brh_reports.repository import (
    build_processed_report_entry,
    load_processed_report_keys,
    load_processed_reports,
    save_markdown,
    save_processed_reports,
)


def test_manifest_roundtrip(tmp_path: Path) -> None:
    manifest_path = tmp_path / "processed_reports.json"
    report = ReportCandidate(
        title="Example Report",
        detail_url="https://example.com/detail",
        pdf_url="https://example.com/report.pdf",
        published_on="25.04.2026",
    )
    entry = build_processed_report_entry(report, Path("reports/markdown/2026/example-report.md"))
    save_processed_reports(manifest_path, {entry["report_key"]: entry})

    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert len(payload["reports"]) == 1
    assert payload["reports"][0]["title"] == "Example Report"
    assert load_processed_report_keys(manifest_path) == {payload["reports"][0]["report_key"]}
    assert load_processed_reports(manifest_path)[payload["reports"][0]["report_key"]]["title"] == "Example Report"


def test_save_markdown_uses_year_folder(tmp_path: Path) -> None:
    report = ReportCandidate(
        title="Example Report",
        detail_url="https://example.com/detail",
        pdf_url="https://example.com/report.pdf",
        published_on="25.04.2026",
    )

    output_path = save_markdown(report, "# Example", tmp_path)

    assert output_path == tmp_path / "2026" / "2026-04-25-example-report.md"
    assert output_path.read_text(encoding="utf-8") == "# Example"


def test_save_markdown_truncates_long_file_names(tmp_path: Path) -> None:
    report = ReportCandidate(
        title="Very Long Report Title " * 20,
        detail_url="https://example.com/detail",
        pdf_url="https://example.com/report.pdf",
        published_on="25.04.2026",
    )

    output_path = save_markdown(report, "# Example", tmp_path)

    assert output_path.parent == tmp_path / "2026"
    assert output_path.suffix == ".md"
    assert len(output_path.stem) < 120
    assert output_path.read_text(encoding="utf-8") == "# Example"
