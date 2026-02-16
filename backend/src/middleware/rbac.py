"""RBAC middleware placeholder."""

def check_user_access(user, policy_owner_id):
    """Return True if user can access the policy; very small stub: user.id == owner or user.role == 'admin'"""
    try:
        return getattr(user, "id", None) == policy_owner_id or getattr(user, "role", None) == "admin"
    except Exception:
        return False
