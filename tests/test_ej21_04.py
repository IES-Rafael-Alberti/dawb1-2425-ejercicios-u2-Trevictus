import pytest
from src.condicionales.ej21_04 import mostrar_par_impar

@pytest.mark.parametrize(
    "numero, expected",
    [
        (0, "El nº es par."),
        (17, "El nº es impar."),
        ("zfsddsf", "El programa no admite cadena de caracteres.")
    ]
)
def test_mostrar_par_impar(numero, expected):
    assert mostrar_par_impar(numero) == expected