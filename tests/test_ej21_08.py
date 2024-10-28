import pytest
from src.condicionales.ej21_08 import *

@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ('0.1', 0.1),#nivel inaceptable
        ('0.45', 0.45),#nivel aceptable
        ('0.71', 0.71)#nivel meritorio
    ]
)
def test_leer_puntuacion(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert leer_puntuacion() == expected


@pytest.mark.parametrize(
    "puntuacion, expected",
    [
        (0.2, "con la puntuacion de 0.2 y un rendimiento inaceptable obtienes de beneficio 480.0"),
        (0.5, "con la puntuacion de 0.5 y un rendimiento aceptable obtienes de beneficio 1200.0"),
        (0.6, "con la puntuacion de 0.6 y un rendimiento meritorio obtienes de beneficio 1440.0"),
        (0.7, "con la puntuacion de 0.7 y un rendimiento meritorio obtienes de beneficio 1440.0"),
        (-1, "ERROR. Puntuación inválida.")
    ]
)
def test_cuantia(puntuacion, expected):
    assert cuantia(puntuacion) == expected