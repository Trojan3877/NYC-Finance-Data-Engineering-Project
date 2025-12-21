from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_prediction():
    response = client.post("/predict", json={"features":[1,2,3]})
    assert response.status_code == 200
