from fastapi.testclient import TestClient
from read_pdf import clean
from main import app

client = TestClient(app)

def test_clean_removes_extra_spaces():
    assert clean ("   hello \n\n   world  ") == "hello world"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_ask_needs_a_question():
    response = client.post("/ask", json={})
    assert response.status_code == 422