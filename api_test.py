import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ev_data_by_year_200_success():
    response = client.get("/ev-data/2023")

    assert response.status_code == 200

    response_data = response.json()
    assert isinstance(response_data, list)

    if len(response_data) > 0:
        assert "make" in response_data[0]
        assert "vehicle_count" in response_data[0]
        assert "average_electric_range" in response_data[0]


def test_ev_data_by_year_not_found():
    response = client.get("/ev-data/1990")

    assert response.status_code == 404
    assert response.json() == {"detail": "No data found for the specified model year"}


def test_ev_data_invalid_model_year():
    response = client.get("/ev-data/invalidyear")

    assert response.status_code == 422
