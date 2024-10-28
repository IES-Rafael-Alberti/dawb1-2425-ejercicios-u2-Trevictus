import pytest
from src.condicionales.ej21_10 import *

@pytest.mark.parametrize(
    "respuesta, expected",
    [
        (1, "Vegetariana"),
        (2, "No vegetariana"),
        (37, "Error, elija entre el 1 y el 2")
    ]
)
def test_preguntar(respuesta, expected):
    assert preguntar(respuesta) == expected