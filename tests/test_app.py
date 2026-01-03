from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_ask_balance_sheet():
    r = client.post("/ask", json={"question": "What is a balance sheet?"})
    assert r.status_code == 200
    assert "balance sheet" in r.json()["answer"].lower()
