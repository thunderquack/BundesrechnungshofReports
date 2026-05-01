from brh_reports.converter import _normalize_legacy_pdf_text, _replacement_char_ratio


def test_replacement_char_ratio() -> None:
    assert _replacement_char_ratio("") == 0.0
    assert _replacement_char_ratio("abc") == 0.0
    assert _replacement_char_ratio("a\ufffdc\ufffd") == 0.5


def test_normalize_legacy_pdf_text() -> None:
    assert _normalize_legacy_pdf_text("einschlieûlich") == "einschließlich"
