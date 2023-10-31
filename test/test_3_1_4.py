import pytest 
from src.E_3_1_4 import *

#test monkeypatch

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (["6","8","1","3","2","4","7","5"],["1","2","3","4","5","6","7","8"])
    ]
)

def test_ordenarMayorMenor(input_x,expected):
    assert ordenarMayorMenor(input_x) == expected