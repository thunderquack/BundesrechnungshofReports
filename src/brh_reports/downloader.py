from __future__ import annotations

from pathlib import Path

from brh_reports.models import DownloadedReport, ReportCandidate


def download_report(candidate: ReportCandidate, target_dir: Path) -> DownloadedReport:
    """Download a single report PDF.

    Placeholder implementation until the concrete download strategy is defined.
    """
    raise NotImplementedError("PDF download is not implemented yet.")
