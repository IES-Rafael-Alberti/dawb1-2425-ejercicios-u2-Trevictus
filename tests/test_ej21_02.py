import pytest
from src.condicionales.ej21_02 import *

@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ("contrASEña", "contraseña"), #
        ("contra", "contra"),
        ("quitina", "quitina"),
        ("contraseña", "contraseña")
    ]
)
def test_pedir_contrasenia(mock_input, expected, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: mock_input)
    assert pedir_contrasenia() == expected



@pytest.mark.parametrize(
    "password, expected",
    [
        ("quico", False),
        ("pepinillo", False),
        ("CONTRAseña", True),
        ("contraseña", True)
    ]
)
def test_comprobar_pass(password, expected):
    assert comprobar_pass(password) == expected