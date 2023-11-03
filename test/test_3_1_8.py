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
    "input_x,expected",
    [
        (True,"La palabra es palíndromo")
    ]
)

def test_mensajeSalidaSi(input_x,expected):
    assert mensajeSalidaSi(input_x) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        (False,"La palabra no es palíndromo")
    ]
)

def test_mensajeSalidaNo(input_x,expected):
    assert mensajeSalidaNo(input_x) == expected