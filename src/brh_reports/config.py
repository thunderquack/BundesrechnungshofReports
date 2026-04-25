from __future__ import annotations

import math
import tempfile
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Settings:
    base_url: str = "https://www.bundesrechnungshof.de/"
    search_url: str = (
        "https://www.bundesrechnungshof.de/SiteGlobals/Forms/Suche/"
        "Berichtssuche/Berichtssuche_Formular.html"
    )
    temp_dir: Path = Path(tempfile.gettempdir()) / "bundesrechnungshof-reports"
    state_dir: Path = Path("state")
    manifest_path: Path = Path("state/processed_reports.json")
    markdown_dir: Path = Path("reports/markdown")
    metadata_dir: Path = Path("reports/metadata")
    results_per_page: int = 50
    headless: bool = True
    user_agent: str = "Mozilla/5.0"
    gtp_page_parameter: str = "20916_list%253D"
    request_delay_seconds: float = 0.5

    def page_url(self, page_number: int) -> str:
        if page_number <= 1:
            return f"{self.search_url}?resultsPerPage={self.results_per_page}"
        return (
            f"{self.search_url}?gtp={self.gtp_page_parameter}{page_number}"
            f"&resultsPerPage={self.results_per_page}"
        )

    def total_pages(self, total_results: int) -> int:
        return math.ceil(total_results / self.results_per_page)


def get_settings() -> Settings:
    return Settings()
