---

description: "Task list for Policy-Aware AI Assistant"

---

# Tasks: Policy-Aware AI Assistant

**Input**: Design documents from `specs/1-policy-aware-assistant/`  
**Prerequisites**: `spec.md` (required), `checklists/requirements.md`

## Phase 1: Setup (Shared Infrastructure)

- [ ] T001 Create feature directory and spec files at specs/1-policy-aware-assistant/spec.md
- [ ] T002 [P] Create feature branch reference at .git/refs/heads/1-policy-aware-assistant
- [ ] T003 [P] Add feature README at specs/1-policy-aware-assistant/README.md

---

## Phase 2: Foundational (Blocking Prerequisites)

- [ ] T004 Setup RAG pipeline scaffold in backend/src/services/rag/index.py
- [ ] T005 [P] Implement vector DB connector in backend/src/services/vector_db.py
- [ ] T006 [P] Implement OCR ingestion service in backend/src/services/ocr.py
- [ ] T007 Implement clause chunker service in backend/src/services/chunker.py
- [ ] T008 Implement RBAC middleware in backend/src/middleware/rbac.py
- [ ] T009 Implement audit logging service in backend/src/services/audit.py
- [ ] T010 Configure environment and secrets example at config/.env.example

**Checkpoint**: Foundational phase complete — RAG, OCR, RBAC, and audit services in place.

---

## Phase 3: User Story 1 - Quick Coverage Lookup (Priority: P1) 🎯 MVP

**Goal**: Allow authenticated users to upload/reference a policy and ask whether a specific loss is covered; responses must include plain-language summary and clause citation.

**Independent Test**: Use `specs/1-policy-aware-assistant/spec.md` sample policy and a claim scenario; verify API returns plain-language answer with clause citation.

### Implementation

- [ ] T011 [P] [US1] Create `Policy` model in backend/src/models/policy.py (attributes: policy_id, owner_id, text, parsed_clauses)
- [ ] T012 [US1] Implement policy upload API endpoint in backend/src/api/policies.py
- [ ] T013 [US1] Implement clause search endpoint in backend/src/api/search.py
- [ ] T014 [P] [US1] Implement plain-language summarizer service in backend/src/services/summarizer.py
- [ ] T015 [US1] Add unit tests for policy upload and clause lookup in tests/unit/test_policy.py


**Checkpoint**: US1 should be independently testable (upload → clause lookup → plain-language answer + citation).

---

## Phase 4: User Story 2 - Claim Type Recommendation (Priority: P2)

**Goal**: Recommend the correct claim type and required forms/data points based on user-provided incident details.

**Independent Test**: Simulate incident descriptions and verify recommendation includes claim type, supporting clause citation, and required fields list.

### Implementation

- [ ] T016 [P] [US2] Create `ClaimRecommendation` model in backend/src/models/claim_recommendation.py
- [ ] T017 [US2] Implement claim recommendation service in backend/src/services/recommender.py
- [ ] T018 [US2] Implement claim recommendation API endpoint in backend/src/api/claims.py
- [ ] T019 [US2] Add integration test for recommendation flow in tests/integration/test_recommender.py

**Checkpoint**: US2 produces a claim recommendation with citation and required-data checklist.

---

## Phase 5: User Story 3 - Estimated Payout Guidance (Priority: P3)

**Goal**: Provide an estimated payout range using policy limits, deductibles, and provided loss details; mark results as estimates requiring human validation.

**Independent Test**: Provide claim scenario and verify estimator returns a calculation rationale, deductible application, and estimation disclaimer.

### Implementation

- [ ] T020 [P] [US3] Implement payout estimator service in backend/src/services/estimator.py
- [ ] T021 [US3] Integrate estimator into claim API at backend/src/api/claims.py (depends on T018, T020)
- [ ] T022 [US3] Add unit tests for estimator in tests/unit/test_estimator.py

**Checkpoint**: US3 returns reproducible estimate with clear disclaimer and citation.

---

## Phase N: Polish & Cross-Cutting Concerns

- [ ] T023 [P] Documentation updates in specs/1-policy-aware-assistant/README.md
- [ ] T024 Create security & compliance checklist at specs/1-policy-aware-assistant/checklists/security.md
- [ ] T025 [P] Create demo script placeholder at scripts/demo/policy_assistant_demo.sh
- [ ] T026 Run end-to-end validation using sample policy and demo script at scripts/demo/policy_assistant_demo.sh

---

## Dependencies & Execution Order

- **Phase Dependencies**:
  - Phase 1 (Setup): no dependency
  - Phase 2 (Foundational): requires Phase 1
  - Phases 3–5 (User Stories): require Phase 2
  - Polish (Final): depends on all user stories

- **User Story Order** (recommended MVP-first): US1 → US2 → US3

## Parallel Opportunities

- Tasks marked `[P]` can run in parallel (example: T005, T006, T014, T016, T020).
- Within US1, T011 (model), T012 (upload API), and T014 (summarizer) can be parallelized once foundational services exist.
- Multiple user stories can be implemented in parallel once foundational tasks complete.

## Parallel Execution Example (User Story 1)

- Run in parallel:
  - `backend/src/models/policy.py` (T011)
  - `backend/src/api/policies.py` (T012)
  - `backend/src/services/summarizer.py` (T014)

## Implementation Strategy

- MVP First: Complete Phase 1 → Phase 2 → Phase 3 (US1). Validate US1 independently, then add US2 and US3.
- Deliver incrementally with checkpoints after each phase.

## Validation

- Each user story phase includes at least: model(s) → service(s) → endpoint(s) → tests.
- Tests should fail before implementation where TDD is applied (optional per spec).

