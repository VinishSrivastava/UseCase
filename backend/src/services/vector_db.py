"""Vector DB connector stub."""

class VectorDB:
    def __init__(self, url: str = None):
        self.url = url

    def upsert(self, vectors):
        # placeholder
        return True

    def query(self, vector, top_k=5):
        # placeholder
        return []
