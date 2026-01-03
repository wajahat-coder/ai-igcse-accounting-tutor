from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI IGCSE Accounting Tutor (scaffold)")

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
async def ask(req: AskRequest):
    q = req.question.strip().lower()
    if "balance sheet" in q:
        answer = "A balance sheet shows assets, liabilities and equity at a point in time."
    elif "profit" in q or "loss" in q:
        answer = "Profit is revenue minus expenses; a loss is when expenses exceed revenue."
    else:
        answer = "I'm a scaffolded tutor. Provide a specific accounting question about transactions, profit/loss, or financial statements."
    return AskResponse(answer=answer)
