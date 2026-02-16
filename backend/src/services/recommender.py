"""Claim recommendation service stub."""

from ..models.claim_recommendation import ClaimRecommendation


def recommend_claim_type(incident_text: str, clauses: list) -> ClaimRecommendation:
    """Simple heuristic recommender: looks for keywords."""
    text = incident_text.lower()
    if "burglary" in text or "theft" in text:
        claim_type = "Burglary/Theft"
        required = ["police_report", "item_list", "proof_of_ownership"]
    elif "water" in text or "flood" in text:
        claim_type = "Water Damage"
        required = ["photos", "repair_estimate"]
    else:
        claim_type = "General Property"
        required = ["description", "photos"]

    return ClaimRecommendation(claim_type=claim_type, supporting_clauses=clauses[:1], required_fields=required)
