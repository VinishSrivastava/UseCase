"""Plain-language summarizer stub."""

def summarize_clause(clause_text: str) -> str:
    """Return a short plain-language 'summary' for a clause (very naive)."""
    # Naive: return first sentence
    if not clause_text:
        return ""
    sentences = clause_text.split('.')
    return (sentences[0] + '.').strip() if sentences else clause_text
