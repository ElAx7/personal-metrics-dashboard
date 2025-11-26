import sys
import os

# Ajustar el path ANTES de cualquier import interno
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from main import app


def test_smoke():
    assert app is not None


client = TestClient(app)

def test_docs_available():
    response = client.get("/docs")
    assert response.status_code == 200

def test_root_status():
    response = client.get("/")
    assert response.status_code in [200, 404]
