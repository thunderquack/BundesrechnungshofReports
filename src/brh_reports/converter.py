from __future__ import annotations

import io
from contextlib import redirect_stdout
from pathlib import Path

import pymupdf4llm


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
    return markdown
