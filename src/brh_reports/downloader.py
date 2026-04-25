from __future__ import annotations

from brh_reports.models import DownloadedReport, ReportCandidate


def download_report(candidate: ReportCandidate) -> DownloadedReport:
    """Download a single report PDF.

    Placeholder implementation until the concrete download strategy is defined.
    The final implementation should keep the PDF in memory and avoid persisting it.
    """
    raise NotImplementedError("PDF download is not implemented yet.")
