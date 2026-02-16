"""Clause chunker stub."""

def clause_level_chunk(text: str):
    """Very small chunker: split by paragraphs and return dicts with ids."""
    chunks = []
    for i, p in enumerate([s.strip() for s in text.split('\n\n') if s.strip()]):
        chunks.append({"id": f"c{i}", "text": p})
    return chunks
