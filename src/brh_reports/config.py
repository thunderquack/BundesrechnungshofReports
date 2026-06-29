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
    user_agent: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    )
    gtp_page_parameter: str = "20916_list%253D"
    request_delay_seconds: float = 0.5

    def request_headers(self) -> dict[str, str]:
        return {
            "User-Agent": self.user_agent,
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,"
                "image/avif,image/webp,*/*;q=0.8"
            ),
            "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        }

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
