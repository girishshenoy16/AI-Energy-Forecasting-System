import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import pytest
from app.energy_app import app


# ---------------------------------------------------------
# FIXTURE: Create a test client for our Flask application
# ---------------------------------------------------------
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ---------------------------------------------------------
# FIXTURE: Automatically mock MODEL.predict() for all tests
# ---------------------------------------------------------
class DummyModel:
    def predict(self, X):
        return [123.45]   # Controlled mocked prediction


@pytest.fixture(autouse=True)
def mock_model(monkeypatch):
    monkeypatch.setattr("app.energy_app.MODEL", DummyModel())


# ---------------------------------------------------------
# TEST 1 — Health Check
# ---------------------------------------------------------
def test_health(client):
    response = client.get("/api/health")
    assert response.status_code == 200

    data = response.get_json()
    assert data["status"] == "running"


# ---------------------------------------------------------
# TEST 2 — /api/predict (Next Hour Prediction)
# ---------------------------------------------------------
def test_predict_next_hour(client):
    payload = {
        "current_energy_usage": 300,
        "temperature_C": 28,
        "humidity_pct": 55,
        "timestamp": "2025-11-19T14:00"
    }

    response = client.post(
        "/api/predict",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 200

    data = response.get_json()

    # ✅ Check response structure
    assert "predicted_energy_next_hour" in data
    assert "model_used" in data
    assert "timestamp" in data

    # ✅ Check prediction value (actual logic check)
    assert isinstance(data["predicted_energy_next_hour"], float)
    assert data["predicted_energy_next_hour"] == 123.45