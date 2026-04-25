from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Settings:
    base_url: str = "https://www.bundesrechnungshof.de/"
    markdown_dir: Path = Path("reports/markdown")
    metadata_dir: Path = Path("reports/metadata")
    headless: bool = True


def get_settings() -> Settings:
    return Settings()
