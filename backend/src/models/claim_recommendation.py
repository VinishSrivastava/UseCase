"""ClaimRecommendation model placeholder"""

from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass
class ClaimRecommendation:
    claim_type: str
    supporting_clauses: List[Dict]
    required_fields: List[str]
    estimated_payout: Optional[float] = None

    def to_dict(self):
        return {
            "claim_type": self.claim_type,
            "supporting_clauses": self.supporting_clauses,
            "required_fields": self.required_fields,
            "estimated_payout": self.estimated_payout,
        }
