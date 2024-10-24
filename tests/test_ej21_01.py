import pytest
from src.condicionales.ej21_01 import *

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
    "edad, expected",
    [
        (15, False), #Edad inválida
        (18, True),  #Edad válida
        (-7, False)  #Edad inválida
    ]
)
def test_comprobar_edad(edad, expected):
    assert comprobar_edad(edad) == expected



@pytest.mark.parametrize(
    "edad, expected",
    [
        (15, "Con la edad de 15 eres menor."), #Edad inválida
        (18, "Con la edad de 18 eres mayor."),  #Edad válida
        (-7, "Con la edad de -7 eres menor.")  #Edad inválida
    ]
)
def test_mostrar_info(edad, expected):
    assert mostrar_info(edad) == expected