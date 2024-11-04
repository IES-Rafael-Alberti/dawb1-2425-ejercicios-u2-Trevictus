import pytest
from src.condicionales.ej21_09 import *

@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ('7 2 ', None),  
        ('-5', -5),    
        ('0', 0),      
        ('cocoliso', None), 
    ]
)
def test_preguntar_edad(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert preguntar_edad() == expected


@pytest.mark.parametrize(
    "edad, expected",
    [
        (3, "Puedes entrar gratis."),
        (15, "Debes pagar 5€ para entrar."), 
        (21, "Debes pagar 10€ para entrar.")
    ]
)
def test_asignar_precio_entrada(edad, expected):
    assert asignar_precio_entrada(edad) == expected