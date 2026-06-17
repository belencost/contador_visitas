import pytest
from src.app import app

@pytest.fixture
def client():
    # Cliente de pruebas simulador
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    # Simula entrar a la página principal y ver si responde bien (código 200)
    response = client.get("/")
    assert response.status_code == 200

def test_api_incrementar(client):
    # Simula hacer un clic para registrarlo
    response = client.post("/clics")
    assert response.status_code == 200
    data = response.get_json()
    assert "total_clics" in data
    assert data["total_clics"] == 1