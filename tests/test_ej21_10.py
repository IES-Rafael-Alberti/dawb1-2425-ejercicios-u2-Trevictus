import pytest
from src.condicionales.ej21_10 import *

@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ('1', "Vegetariana"),  
        ('2', "No vegetariana"),    
        ('3', "Error, elija entre el 1 y el 2"),      
        ('abcdef', "Error, elija entre el 1 y el 2"), 
    ]
)
def test_preguntar(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert preguntar() == expected