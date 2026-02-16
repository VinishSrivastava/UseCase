"""RAG pipeline scaffold (stub)"""

def retrieve_relevant_clauses(query: str, policy_text: str, top_k: int = 5):
    """Stub retrieval: naive substring search over policy_text split by paragraphs."""
    paragraphs = [p.strip() for p in policy_text.split('\n\n') if p.strip()]
    matches = [p for p in paragraphs if query.lower() in p.lower()]
    return matches[:top_k]
