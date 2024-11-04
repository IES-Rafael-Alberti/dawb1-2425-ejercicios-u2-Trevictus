import pytest
from src.condicionales.ej21_06 import *

@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ('Carlos', 'Carlos'),
        ('Manu', 'Manu'),
        ('David', 'David'),
        ('C-3PO', 'C-3PO'), 
    ]
)
def test_preguntar_nombre(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert preguntar_nombre() == expected


@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ('hombre', 'hombre'),
        ('mujer', 'mujer'),
        ('asdf', 'asdf') 
    ]
)
def test_preguntar_sexo(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert preguntar_sexo() == expected


@pytest.mark.parametrize(
    "nombre, sexo, expected",
    [
        ("Rocío", "mujer", "Perteneces al grupo B."),
        ("Ambrosia", "mujer", "Perteneces al grupo A."),
        ("David", "hombre", "Perteneces al grupo B."),
        ("Xenón", "hombre", "Perteneces al grupo A."),
        ("C-3PO", "Robot", "Sexo no válido.")
    ]
)
def test_asignar_clase(nombre, sexo, expected):
    assert asignar_clase(nombre, sexo) == expected