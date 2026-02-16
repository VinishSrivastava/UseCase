"""Payout estimator stub."""

def estimate_payout(policy_limits: dict, loss_amount: float, deductible: float = 0.0) -> dict:
    """Return a simple estimate applying deductible and limits."""
    after_deductible = max(0.0, loss_amount - deductible)
    limit = policy_limits.get("limit", None)
    paid = after_deductible if limit is None else min(after_deductible, limit)
    return {"estimated_payout": paid, "applied_deductible": deductible, "limit": limit}
