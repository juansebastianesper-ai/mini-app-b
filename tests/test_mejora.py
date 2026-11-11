from fastapi.testclient import TestClient

from app.main import app

cliente = TestClient(app)


def test_obtener_unidades():
    respuesta = cliente.get("/api/unidades")

    assert respuesta.status_code == 200
    assert respuesta.json() == {
        "temperatura": ["C", "F", "K"],
        "longitud": ["mm", "cm", "m", "km"],
        "masa": ["g", "kg", "lb"],
    }
