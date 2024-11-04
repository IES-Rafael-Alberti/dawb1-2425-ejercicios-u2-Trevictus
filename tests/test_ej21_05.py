import pytest
from src.condicionales.ej21_05 import *

@pytest.mark.parametrize(
    "mock_input, expected",
    [
        (' 1 0', None),   # Número positivo válido
        ('-5', -5),     # Número negativo válido
        ('0', 0),       # Número cero
        ('palabra', None), 
    ]
)
def test_preguntar_edad(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert preguntar_edad() == expected


@pytest.mark.parametrize(
    "mock_input, expected",
    [
        (' 1 0', None),   # Número positivo válido
        ('-5', -5),     # Número negativo válido
        ('0', 0),       # Número cero
        ('palabra', None),
        ('150.0', 150.0) 
    ]
)
def test_preguntar_ingresos(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert preguntar_ingresos() == expected


@pytest.mark.parametrize(
    "edad, ingresos, expected",
    [
        (15, 500, "No tributas"),
        (15, 1000, "No tributas"),
        (18, 500, "No tributas"),
        (18, 1000, "Tributas")
    ]
)
def test_mostrar_tributacion(edad, ingresos, expected):
    assert mostrar_tributacion(edad, ingresos) == expected