import json
import pytest
from unittest.mock import MagicMock
from app.energy_app import app, MODEL


# ---------------------------------------------------------
# FIXTURE: Create a test client for our Flask application
# ---------------------------------------------------------
@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


# ---------------------------------------------------------
# FIXTURE: Automatically mock MODEL.predict() for all tests
# ---------------------------------------------------------
@pytest.fixture(autouse=True)
def mock_model():
    MODEL.predict = MagicMock(return_value=[123.45])   # Fake prediction output
    return MODEL


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
    assert "predicted_energy_next_hour" in data
    assert data["predicted_energy_next_hour"] == 123.45  # Mocked value
    assert "model_used" in data
    assert "timestamp" in data


# Run using pytest -v commands in virtual envirnonment.