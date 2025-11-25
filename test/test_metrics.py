from fastapi.testclient import TestClient
import sys
import os

# Agregar la ruta raíz del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)

def test_create_metric():
    payload = {
        "datetime": "2025-02-12T10:00:00",
        "category": "gym",
        "value": 120,
        "note": "prueba"
    }

    response = client.post("/metrics", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["category"] == "gym"
    assert data["value"] == 120

def test_get_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_metric():
    update = {
        "value": 150,
        "note": "actualizado desde pytest"
    }

    response = client.put("/metrics/1", json=update)
    assert response.status_code == 200
    data = response.json()
    assert data["value"] == 150


def test_delete_metric():
    response = client.delete("/metrics/1")
    assert response.status_code == 200
    assert response.json()["detail"] == "Metric deleted"

