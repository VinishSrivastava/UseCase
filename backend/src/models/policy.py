"""Policy model placeholder"""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Policy:
    policy_id: str
    owner_id: str
    text: str
    parsed_clauses: List[Dict]

    def find_clauses(self, query: str):
        """Very small stub: return clauses that match query substring."""
        return [c for c in self.parsed_clauses if query.lower() in (c.get("text") or "").lower()]
