"""Minimal clause search API endpoint stub."""

from http.server import BaseHTTPRequestHandler
import json
from ..services.rag.index import retrieve_relevant_clauses


class SearchHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length) if length else b''
        try:
            data = json.loads(body.decode('utf-8'))
        except Exception:
            data = {}
        query = data.get('query', '')
        policy_text = data.get('policy_text', '')
        matches = retrieve_relevant_clauses(query, policy_text)
        resp = {'matches': matches}
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(resp).encode('utf-8'))
