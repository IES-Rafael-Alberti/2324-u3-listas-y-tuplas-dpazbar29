import pytest 
from src.E_3_1_4 import *

def test_pedirNumeros(monkeypatch):
    input_values = [1,78,53,12,21,89,98,3]
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr("builtins.input",mock_input)
    assert pedirNumeros() == [1,78,53,12,21,89,98,3]

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ([6,8,1,3,2,4,7,5],[1,2,3,4,5,6,7,8])
    ]
)

def test_ordenarMayorMenor(input_x,expected):
    assert ordenarMayorMenor(input_x) == expected