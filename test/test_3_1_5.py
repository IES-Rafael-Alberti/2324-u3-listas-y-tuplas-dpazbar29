import pytest
from src.E_3_1_5 import *

@pytest.mark.parametrize(
    "inpput_x,expected",
    [
        ([1,2,3,4,5,6,7,8,9,10],"10,9,8,7,6,5,4,3,2,1")
    ]
)

def test_mostrar(inpput_x,expected):
    assert mostrar(inpput_x) == expected