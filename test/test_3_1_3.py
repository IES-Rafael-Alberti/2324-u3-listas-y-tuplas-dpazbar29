import pytest 
from src.E_3_1_3 import *

#def test_mostrarAsignaturasNotas(monkeypatch):
    #monkeypatch.


@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        (["matemáticas","física","química","historia","lengua"],[1,2,3,4,5],"En matemáticas has sacado un 1\nEn física has sacado un 2\nEn química has sacado un 3\nEn historia has sacado un 4\nEn lengua has sacado un 5")
    ]
)

def test_mensajeSalida(input_x,input_y,expected):
    assert mensajeSalida(input_x,input_y) == expected