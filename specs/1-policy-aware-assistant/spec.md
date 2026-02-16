# Feature Specification: Policy-Aware AI Assistant

**Feature Branch**: `1-policy-aware-assistant`  
**Created**: 2026-02-16  
**Status**: Draft  
**Input**: User description: "Policy-Aware AI Assistant"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Quick Coverage Lookup (Priority: P1)
A policyholder uploads or references their policy and asks whether a specific loss is covered.

**Why this priority**: High-frequency, high-value customer question that reduces call volume.

**Independent Test**: Provide a sample policy and a claim scenario; verify the assistant returns a plain-language coverage answer with a clause citation and one suggested next step.

**Acceptance Scenarios**:
1. Given a valid authenticated user and an uploaded policy, When the user asks "Is water damage from an overflowing dishwasher covered?", Then the assistant returns "Covered / Not covered" with the specific clause citation and an explanation in plain language.
2. Given a partially scanned policy (OCR errors), When the assistant cannot find definitive clause text, Then it replies with "Unable to determine from provided policy" and suggests next steps (upload clearer copy or ask human).

---

### User Story 2 - Claim Type Recommendation (Priority: P2)
The user describes an incident; the assistant recommends the most appropriate claim type and required forms.

**Why this priority**: Reduces wrong-claim submissions and downstream rework.

**Independent Test**: Simulate user incident descriptions and verify the assistant recommends a claim type, cites the supporting clause, and lists required data points.

**Acceptance Scenarios**:
1. Given a burglary incident description, When the user provides date/time and affected items, Then the assistant recommends "Burglary / Theft" claim type, cites the relevant policy clause, and lists required fields/forms.

---

### User Story 3 - Estimated Payout Guidance (Priority: P3)
The assistant provides an estimated payout range based on policy limits, deductibles, and provided loss details.

**Why this priority**: Improves transparency and sets realistic expectations.

**Independent Test**: Provide a claim scenario and verify the assistant returns an estimate with calculation rationale and a clear disclaimer that this is an estimate requiring human validation.

**Acceptance Scenarios**:
1. Given claim details and policy limits, When the assistant estimates payout, Then it includes the deductible deduction, reference to the clause, and marks the result as "estimate" requiring human validation.

---

### Edge Cases
- When policy language is ambiguous or contradictory, the assistant must flag ambiguity and recommend human review.
- When user is unauthenticated or requests another user's policy, deny access and prompt for correct authentication.

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: The system MUST translate policy clauses into plain-language summaries on request.
- **FR-002**: The system MUST accept user questions about limits, deductibles, and exclusions and return clause-backed answers.
- **FR-003**: The system MUST include a specific clause citation (page/clause ID) in every coverage answer.
- **FR-004**: The system MUST recommend the most appropriate claim type based on user-provided incident details.
- **FR-005**: The system MUST provide an estimated payout and clearly label it as an estimate requiring human validation.
- **FR-006**: The system MUST identify required forms/data points to initiate a claim for the recommended type.
- **FR-007**: The system MUST enforce RBAC so users can only access policies tied to their authenticated profile.
- **FR-008**: The system MUST log all interactions (query, retrieved context, response, citations) for audit purposes.

### Key Entities
- **Policy Document**: Represents the uploaded or referenced insurance policy (attributes: policy ID, owner ID, text, parsed clauses).
- **User Session**: Represents an authenticated user interaction (attributes: user ID, role, queries, timestamps).
- **Claim Recommendation**: Represents a recommended claim type and associated metadata (attributes: claim type, supporting clauses, required fields, estimated payout).

## Success Criteria *(mandatory)*

### Measurable Outcomes
- **SC-001**: Reduce basic policy-related call volume by X% (measure baseline then target; initial target: 20%).
- **SC-002**: Increase first-time-right claim submissions (reduce wrong-claim rejections) by Y% (initial target: 30% reduction in wrong-claim rejections).
- **SC-003**: 90% of assistant responses regarding coverage include a direct clause citation.
- **SC-004**: Users report improved clarity (CSAT related to policy questions increases by Z points; initial target: +10 points).

---

## Technical Requirements

### Frontend
- Platforms: Native Mobile (Flutter) or Web (React).
- UI Pattern: Conversational, chat-based interface.

### AI & Data Layer
- LLM: Integration with OpenAI, Azure OpenAI, or Anthropic.
- RAG Framework: LangChain or LlamaIndex for document retrieval.
- Vector DB: Pinecone, Weaviate, or FAISS for clause search.

### Document Processing
- OCR & Parsing: AWS Textract or Azure Form Recognizer for PDFs and forms.
- Chunking: Clause-level chunking to preserve legal context.

### Integrations
- PAS: For real-time policy detail retrieval.
- Claims Management System: To push recommended claims into processing.
- Authentication: Integrate with existing User Profile/Auth systems.

## Assumptions
- Policies include identifiable clause IDs or page numbers for citation.
- RBAC and authentication systems are available and integrable.
- A sample ground-truth test set exists to validate RAG retrieval accuracy.

## Open Questions
- None required now; specifics can be refined during planning.

## Notes
- All payout figures are estimates and require human validation before claim submission.

