import pytest 
from src.E_3_1_10 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ([50, 75, 46, 22, 80, 65, 8],80)
    ]
)

def test_maximo(input_x,expected):
    assert maximo(input_x) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        ([50, 75, 46, 22, 80, 65, 8],8)
    ]
)

def test_minimo(input_x,expected):
    assert minimo(input_x) == expected