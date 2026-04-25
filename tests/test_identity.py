from brh_reports.identity import build_report_identity_value, build_report_key
from brh_reports.models import ReportCandidate


def test_report_key_uses_title_and_published_date() -> None:
    candidate = ReportCandidate(
        title="Report Title",
        detail_url="https://example.com/detail",
        pdf_url="https://example.com/report.pdf",
        published_on="25.04.2026",
    )

    assert build_report_identity_value(candidate) == "Report Title\n25.04.2026"
    assert len(build_report_key(candidate)) == 64


def test_report_key_changes_when_date_changes() -> None:
    first = ReportCandidate(
        title="Same Title",
        detail_url="https://example.com/detail-1",
        published_on="01.01.2026",
    )
    second = ReportCandidate(
        title="Same Title",
        detail_url="https://example.com/detail-2",
        published_on="02.01.2026",
    )

    assert build_report_key(first) != build_report_key(second)
