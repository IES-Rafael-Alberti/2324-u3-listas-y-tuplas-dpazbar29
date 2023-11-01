import pytest 
from src.E_3_1_6 import *

#monkeypatch pedir notas

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