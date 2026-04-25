from __future__ import annotations

import hashlib

from brh_reports.models import ReportCandidate


def build_report_identity_value(candidate: ReportCandidate) -> str:
    title = " ".join(candidate.title.split()).strip()
    published_on = (candidate.published_on or "").strip()
    return f"{title}\n{published_on}"


def build_report_key(candidate: ReportCandidate) -> str:
    identity_value = build_report_identity_value(candidate)
    return hashlib.sha256(identity_value.encode("utf-8")).hexdigest()
