from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "API running"}

def test_prediction_with_mock_model():
    mock_model = MagicMock()
    mock_model.predict.return_value = [42.0]

    with patch("api.main._get_model", return_value=mock_model):
        response = client.post("/predict", json={"features": [1.0, 2.0, 3.0]})

    assert response.status_code == 200
    assert response.json() == {"prediction": 42.0}

def test_prediction_missing_model():
    with patch("api.main._get_model", side_effect=FileNotFoundError("no model")):
        response = client.post("/predict", json={"features": [1.0, 2.0, 3.0]})
    assert response.status_code == 503
