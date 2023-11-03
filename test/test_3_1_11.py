import pytest 
from src.E_3_1_11 import *

@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        ([1,2,3],[-1,0,2],5)
    ]
)

def test_calculoProductoEscalar(input_x,input_y,expected):
    assert calculoProductoEscalar(input_x,input_y) == expected


@pytest.mark.parametrize(
    "input_x,input_y,input_z,expected",
    [
        ([1,2,3],[-1,0,2],5,"El resultado del producto escalar de: [1, 2, 3] + [-1, 0, 2] = 5")
    ]
)

def test_mensajeSalida(input_x,input_y,input_z,expected):
    assert mensajeSalida(input_x,input_y,input_z) == expected