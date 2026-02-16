"""Audit logging stub."""

def log_interaction(user_id: str, query: str, retrieved: list, response: str, citations: list):
    """Append a simple audit record to a local file (placeholder)."""
    record = {
        "user_id": user_id,
        "query": query,
        "retrieved": retrieved,
        "response": response,
        "citations": citations,
    }
    try:
        with open("./audit.log", "a", encoding="utf-8") as f:
            f.write(str(record) + "\n")
    except Exception:
        pass
