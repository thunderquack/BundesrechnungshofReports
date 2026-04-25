from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ReportCandidate:
    title: str
    detail_url: str
    pdf_url: str | None = None


@dataclass(slots=True)
class DownloadedReport:
    title: str
    source_url: str
    pdf_path: str
