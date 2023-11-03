import pytest 
from src.E_3_1_2 import *


@pytest.mark.parametrize(
        "input_x,expected",
        [
            (["matemáticas","física","química","historia","lengua"],"Yo estudio matemáticas\nYo estudio física\nYo estudio química\nYo estudio historia\nYo estudio lengua")
        ]
)
def test_mostrarAsignaturas(input_x,expected):
    assert mostrarAsignaturas(input_x) == expected