from __future__ import annotations

import io
from contextlib import redirect_stdout
from pathlib import Path

import fitz
import pymupdf4llm

MAX_REPLACEMENT_CHAR_RATIO = 0.05


def _replacement_char_ratio(text: str) -> float:
    if not text:
        return 0.0
    return text.count("\ufffd") / len(text)


def _normalize_legacy_pdf_text(text: str) -> str:
    return text.replace("û", "ß")


def _convert_pdf_to_plain_markdown(pdf_path: Path) -> str:
    pages: list[str] = []
    with fitz.open(pdf_path) as document:
        for page_index, page in enumerate(document, start=1):
            text = _normalize_legacy_pdf_text(page.get_text("text")).strip()
            if not text:
                continue
            pages.append(f"<!-- page {page_index} -->\n\n{text}")
    return "\n\n---\n\n".join(pages)


def convert_pdf_to_markdown(pdf_path: Path) -> str:
    """Convert a PDF file into Markdown text."""
    with redirect_stdout(io.StringIO()):
        markdown = pymupdf4llm.to_markdown(
            str(pdf_path),
            show_progress=False,
            force_text=True,
    )
    if not isinstance(markdown, str):
        raise TypeError(f"Unexpected Markdown output type: {type(markdown)!r}")
    if _replacement_char_ratio(markdown) > MAX_REPLACEMENT_CHAR_RATIO:
        return _convert_pdf_to_plain_markdown(pdf_path)
    return markdown
