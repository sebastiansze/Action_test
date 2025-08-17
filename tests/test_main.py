import sys
from pathlib import Path

# Projektwurzel dem sys.path hinzufügen
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app  # importiert app.py von oberster Ebene
from fastapi.testclient import TestClient

client = TestClient(app)

def test_compute():
    response = client.post("/compute", json={"value": 555})
    assert response.status_code == 200
    assert response.json() == {"result": 1000}
