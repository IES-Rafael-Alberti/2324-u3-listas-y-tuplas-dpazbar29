import pytest 
from src.E_3_1_12 import *

@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        ([[1,2,3],[4,5,6]],[[-1,0],[0,1],[1,1]],[[2,5],[2,11]])
    ]
)

def test_productoMatrices(input_x,input_y,expected):
    assert productoMatrices(input_x,input_y) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        ([[2,5],[2,11]],"El resultado es: [[2, 5], [2, 11]]")
    ]
)

def test_mensajeSalida(input_x,expected):
    assert mensajeSalida(input_x) == expected