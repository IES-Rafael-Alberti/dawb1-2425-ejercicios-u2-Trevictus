import pytest
from src.condicionales.ej21_07 import *

@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ('15000.467', 15000.467),
        ('1000', 1000),
        ('0.71', 0.71)
    ]
)
def test_preguntar_renta_anual(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert preguntar_renta_anual() == expected



@pytest.mark.parametrize(
    "cuantia, expected",
    [
        (9000, "Tus impuestos son del 5%."),
        (15000, "tus impuestos son del 15%."),
        (26000.43, "Tus impuestos son del 20%."),
        (42500.31, "Tus impuestos son del 30%."),
        (100000.12, "Tus impuestos son del 45%.")
    ]
)
def test_mostrar_tipo_impositivo(cuantia, expected):
    assert mostrar_tipo_impositivo(cuantia) == expected