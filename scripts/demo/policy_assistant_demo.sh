#!/usr/bin/env bash
# Demo script placeholder for Policy-Aware AI Assistant
# Usage: ./scripts/demo/policy_assistant_demo.sh

set -euo pipefail

echo "This is a demo placeholder for the Policy-Aware AI Assistant."

# Example: Start backend (development)
# Run: uvicorn backend.app:app --reload --port 8000

# Example: Upload a sample policy (sends file name as policy_id)
curl -s -X POST "http://localhost:8000/api/policies" -F "file=@sample_policy.txt" | jq .

# Example: Run a search against policy text
curl -s -X POST "http://localhost:8000/api/search" -H "Content-Type: application/json" -d '{"query":"water damage","policy_text":"Water damage is excluded. Theft is covered."}' | jq .

# Example: Ask for claim recommendation and estimate
curl -s -X POST "http://localhost:8000/api/claims" -H "Content-Type: application/json" -d '{"incident":"There was a burglary and items were stolen","clauses":[],"policy_limits":{"limit":5000},"loss_amount":3000,"deductible":100}' | jq .

echo "Demo run complete. Start the server with uvicorn backend.app:app --reload --port 8000 and ensure sample_policy.txt exists."
