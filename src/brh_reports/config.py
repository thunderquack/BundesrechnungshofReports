from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Settings:
    base_url: str = "https://www.bundesrechnungshof.de/"
    search_url: str = (
        "https://www.bundesrechnungshof.de/SiteGlobals/Forms/Suche/"
        "Berichtssuche/Berichtssuche_Formular.html"
    )
    temp_dir: Path = Path("data/tmp")
    markdown_dir: Path = Path("reports/markdown")
    metadata_dir: Path = Path("reports/metadata")
    results_per_page: int = 50
    headless: bool = True
    user_agent: str = "Mozilla/5.0"


def get_settings() -> Settings:
    return Settings()
