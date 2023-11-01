import pytest 
from src.E_3_1_8 import *


@pytest.mark.parametrize(
        "input_x,expected",
        [
            ("reconocer",True),
            ("sala",False)
        ]
)

def test_palindromo(input_x,expected):
    assert palindromo(input_x) == expected



@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        (True,"reconocer","La palabra reconocer es palíndromo"),
        (False,"sala","La palabra sala no es palíndromo")
    ]
)

def test_mensajeSalida(input_x,input_y,expected):
    assert mensajeSalida(input_x,input_y) == expected