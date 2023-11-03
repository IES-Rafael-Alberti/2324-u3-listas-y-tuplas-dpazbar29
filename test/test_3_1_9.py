import pytest 
from src.E_3_1_9 import *

@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        ("murcielago",["a","e","i","o","u"],[1,1,1,1,1])
    ]
)

def test_contarVocales(input_x,input_y,expected):
    assert contarVocales(input_x,input_y) == expected


@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        ([1,1,1,1,1],["a","e","i","o","u"],"La vocal a aparece 1\nLa vocal e aparece 1\nLa vocal i aparece 1\nLa vocal o aparece 1\nLa vocal u aparece 1\n")
    ]
)

def test_mensajeSalida(input_x,input_y,expected):
    assert mensajeSalida(input_x,input_y) == expected