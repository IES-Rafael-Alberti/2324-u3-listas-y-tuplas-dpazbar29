import pytest 
from src.E_3_1_1 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (["Matemáticas","Física","Química","Historia","Lengua"],"Matemáticas,Física,Química,Historia,Lengua")
    ]
)

def test_mostrarAsignaturas(input_x,expected):
    assert mostrarAsignaturas(input_x) == expected