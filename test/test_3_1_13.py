import pytest 
from src.E_3_1_13 import *

'''
def test_pedirNumeros(monkeypatch):
    input_values = [1,2,3,"a"]
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr("builtins.input",mock_input)
    assert pedirNumeros() == [1,2,3]
'''

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ([1,2,3],2.0)
    ]
)

def test_media(input_x,expected):
    assert media(input_x) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        ([1,2,3],0.82)
    ]
)

def test_desviacionTipica(input_x,expected):
    assert desvicionTipica(input_x) == expected


@pytest.mark.parametrize(
    "input_x,input_y,input_z,expected",
    [
        ([1,2,3],2.0,0.82,"La media de 6 es: 2.0 y la desviación típica es: 0.82")
    ]
)

def test_mensajeSalida(input_x,input_y,input_z,expected):
    assert mensajeSalida(input_x,input_y,input_z) == expected


