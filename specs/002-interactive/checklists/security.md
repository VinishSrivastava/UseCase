# Security & Compliance Checklist: Policy-Aware AI Assistant

**Purpose**: Ensure security, privacy, and compliance controls are considered for the feature
**Created**: 2026-02-17

## Access Control
- [ ] RBAC enforced for all policy access
- [ ] Least-privilege applied to service accounts and APIs
- [ ] MFA required for privileged roles

## Data Protection
- [ ] Policy documents encrypted at rest
- [ ] Transport-level encryption (TLS) for all endpoints
- [ ] PII detection and redaction for logs and exported artifacts

## Audit & Logging
- [ ] All AI interactions logged with query, retrieved context, response, and citations
- [ ] Immutable audit trail retention policy defined
- [ ] Alerts for anomalous access patterns

## Privacy & Retention
- [ ] Data retention policy for uploaded policies and interaction logs
- [ ] Deletion procedure for user-requested data removal

## Risk & Testing
- [ ] Threat model completed for RAG pipeline and document ingestion
- [ ] Penetration test scheduled prior to production
- [ ] Ground-truth tests for hallucination mitigation included in CI

## Compliance
- [ ] Verify legal/regulatory requirements for policy data handling
- [ ] Data transfer agreements in place for third-party services (e.g., OCR, vector DB)

## Notes
- Items must be reviewed by Security and Privacy stakeholders before production rollout.
