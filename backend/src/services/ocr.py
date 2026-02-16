"""OCR ingestion service stub."""

def extract_text_from_pdf(path: str) -> str:
    """Stub that would call OCR provider; returns file contents for now."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""
