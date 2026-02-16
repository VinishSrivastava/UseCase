from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

from backend.src.services.rag.index import retrieve_relevant_clauses
from backend.src.services.recommender import recommend_claim_type
from backend.src.services.estimator import estimate_payout
from backend.src.services.ocr import extract_text_from_pdf
from backend.src.services.chunker import clause_level_chunk
from backend.src.services.summarizer import summarize_clause

app = FastAPI(title="Policy-Aware AI Assistant (dev)")


class UploadResponse(BaseModel):
    policy_id: str


@app.post("/api/policies", response_model=UploadResponse)
async def upload_policy(file: UploadFile = File(...)):
    # save file temporarily and run OCR (stub)
    try:
        content = await file.read()
        # write to temp
        tmp_path = f"/tmp/{file.filename}"
        with open(tmp_path, "wb") as f:
            f.write(content)
        text = extract_text_from_pdf(tmp_path)
        clauses = clause_level_chunk(text)
        # return a synthetic policy id
        return {"policy_id": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SearchRequest(BaseModel):
    query: str
    policy_text: str


@app.post("/api/search")
def search(req: SearchRequest):
    matches = retrieve_relevant_clauses(req.query, req.policy_text)
    summaries = [summarize_clause(m) for m in matches]
    return {"matches": matches, "summaries": summaries}


class ClaimsRequest(BaseModel):
    incident: str
    clauses: list = []
    policy_limits: dict = {}
    loss_amount: float = 0.0
    deductible: float = 0.0


@app.post("/api/claims")
def claims(req: ClaimsRequest):
    rec = recommend_claim_type(req.incident, req.clauses)
    payout = estimate_payout(req.policy_limits, req.loss_amount, req.deductible)
    return {"recommendation": rec.to_dict(), "payout_estimate": payout}
