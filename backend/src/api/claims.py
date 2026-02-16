"""Minimal claim recommendation & estimator API endpoint stub."""

from http.server import BaseHTTPRequestHandler
import json
from ..services.recommender import recommend_claim_type
from ..services.estimator import estimate_payout


class ClaimsHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length) if length else b''
        try:
            data = json.loads(body.decode('utf-8'))
        except Exception:
            data = {}

        incident = data.get('incident', '')
        clauses = data.get('clauses', [])
        rec = recommend_claim_type(incident, clauses)
        payout = estimate_payout(data.get('policy_limits', {}), data.get('loss_amount', 0.0), data.get('deductible', 0.0))
        resp = {"recommendation": rec.to_dict(), "payout_estimate": payout}
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(resp).encode('utf-8'))
