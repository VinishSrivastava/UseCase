"""Minimal API endpoint stubs for policies."""

from http.server import BaseHTTPRequestHandler
import json
from ..models.policy import Policy


class PolicyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Very small stub: accept JSON body with policy text and return an id
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length) if length else b''
        try:
            data = json.loads(body.decode('utf-8'))
        except Exception:
            data = {}
        policy_id = data.get('policy_id', 'policy-1')
        response = {'policy_id': policy_id}
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))
