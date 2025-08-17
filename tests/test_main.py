from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_compute():
    response = client.post("/compute", json={"value": 555})
    assert response.status_code == 200
    assert response.json() == {"result": 1000}
