import pytest
from src.condicionales.ej21_03 import *

@pytest.mark.parametrize(
    "mock_input, expected",
    [
        (["0", "1"], [0.0, 1.0]), #Entradas válidas
        (["10", "2"], [10.0, 2.0]),
        (["asdffge", "0", "1"], [0.0, 1.0]), #entrada no válida
        (["", "0", "1"], [0.0, 1.0]) #entrada no válida
    ]
)
def test_pedir_numeros(mock_input, expected, monkeypatch):
    inputs = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert pedir_numeros() == expected



@pytest.mark.parametrize(
    "lista_num, expected",
    [
        ([6, 2], "La división del 1er nº entre el 2º da como resultado: 3.0"),
        ([10, 0], "Introducir un cero como divisor no es posible de operar.")
    ]
)
def test_mostrar_division(lista_num, expected):
    global numeros
    numeros[:] = lista_num
    assert mostrar_division() == expected