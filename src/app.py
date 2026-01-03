from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os
from dotenv import load_dotenv

from .llm import LLMClient

load_dotenv()

app = FastAPI(title="AI IGCSE Accounting Tutor")
llm = LLMClient()

HTML = '''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AI IGCSE Accounting Tutor</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; background: #f9f9f9; }
    h1 { color: #333; }
    textarea { width: 100%; padding: 10px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px; }
    button { background: #0066cc; color: white; padding: 10px 20px; border: none; cursor: pointer; border-radius: 4px; font-size: 16px; }
    button:hover { background: #0052a3; }
    pre { background: #f0f0f0; padding: 10px; border-radius: 4px; overflow-x: auto; max-height: 300px; }
  </style>
</head>
<body>
  <h1>🎓 AI IGCSE Accounting Tutor</h1>
  <form id="form">
    <label><strong>Ask a question:</strong></label><br/>
    <textarea id="q" placeholder="What is a balance sheet?" rows="3"></textarea><br/><br/>
    <button type="submit">Ask</button>
  </form>
  <h3>Answer:</h3>
  <pre id="ans">(waiting...)</pre>
  <script>
    document.getElementById('form').onsubmit = async (e) => {
      e.preventDefault();
      const q = document.getElementById('q').value.trim();
      if (!q) return;
      document.getElementById('ans').textContent = 'Loading...';
      try {
        const r = await fetch('/ask', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({question:q}) });
        const d = await r.json();
        document.getElementById('ans').textContent = d.answer;
      } catch (e) { document.getElementById('ans').textContent = 'Error: ' + e; }
    };
  </script>
</body>
</html>'''

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str

@app.get("/", response_class=HTMLResponse)
async def root():
    return HTML

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/ask", response_model=AskResponse)
async def ask(req: AskRequest):
    q = req.question.strip().lower()
    try:
        if llm.available:
            prompt = f"You are an IGCSE accounting tutor. Answer concisely: {req.question}"
            answer = llm.answer(prompt)
            return AskResponse(answer=answer)
    except Exception:
        pass
    
    if "balance sheet" in q:
        answer = "A balance sheet shows the financial position (assets, liabilities, equity) at a specific date."
    elif "profit" in q or "loss" in q:
        answer = "Profit = Revenue - Expenses. Loss occurs when expenses exceed revenue."
    elif "accounting" in q or "account" in q:
        answer = "Accounting is recording and reporting financial transactions to provide useful information."
    elif "debit" in q or "credit" in q:
        answer = "Debit (left) and Credit (right) are two sides of accounting entries. Every transaction affects both."
    else:
        answer = "Ask me about balance sheets, profit/loss, accounting principles, or financial statements!"
    return AskResponse(answer=answer)
