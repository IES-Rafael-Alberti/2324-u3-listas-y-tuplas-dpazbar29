from src.E_3_1_6 import *
import pytest 


def test_pedirNotas(monkeypatch):
    input_values = [1]
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr("builtins.input",mock_input)
    assert pedirNotas(input_values) == [1]


@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        (["matemáticas","física","química","historia","lengua"],[1,2,6,8,9],["matemáticas","física"])
    ]
)

def test_asignaturasSuspensas(input_x,input_y,expected):
    assert asignaturasSuspensas(input_x,input_y) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        (["matemáticas","física"],"Tienes que repetir matemáticas\nTienes que repetir física")
    ]
)

def test_mensajeSalida(input_x,expected):
    assert mensajeSalida(input_x) == expected