import pytest
from fastapi.testclient import TestClient

from app.main import app


cliente = TestClient(app)


def convertir(tipo, valor, de, a):
    return cliente.get(
        "/api/convertir",
        params={"tipo": tipo, "valor": valor, "de": de, "a": a},
    )


def test_pagina_principal():
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert "text/html" in respuesta.headers["content-type"]


def test_celsius_a_fahrenheit():
    respuesta = convertir("temperatura", 100, "C", "F")
    assert respuesta.status_code == 200
    assert respuesta.json()["resultado"] == pytest.approx(212)


def test_celsius_a_kelvin():
    assert convertir("temperatura", 0, "C", "K").json()["resultado"] == pytest.approx(
        273.15
    )


def test_kilometros_a_metros():
    assert convertir("longitud", 1.5, "km", "m").json()["resultado"] == pytest.approx(
        1500
    )


def test_kilogramos_a_libras():
    resultado = convertir("masa", 1, "kg", "lb").json()["resultado"]
    assert resultado == pytest.approx(2.2046, abs=0.001)


def test_misma_unidad():
    assert convertir("longitud", 5, "m", "m").json()["resultado"] == pytest.approx(5)


def test_unidad_no_valida():
    assert convertir("temperatura", 10, "X", "C").status_code == 400


def test_unidades_de_tipos_distintos():
    assert convertir("longitud", 10, "kg", "m").status_code == 400