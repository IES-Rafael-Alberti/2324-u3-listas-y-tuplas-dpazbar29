import pytest 
from src.E_3_1_7 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"],["a","b","d","e","f","h","i","j","l","m","n","o","p","q","s","t","u","w","x","y","z"])
    ]
)

def test_sacarLetras(input_x,expected):
    assert sacarLetras(input_x) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        (["a","b","d","e","f","h","i","j","l","m","n","o","p","q","s","t","u","w","x","y","z"],"Las letras del abecedario cuya posición no son números múltiplos de 3 son: a,b,d,e,f,h,i,j,l,m,n,o,p,q,s,t,u,w,x,y,z")
    ]
)

def test_mensajeSalida(input_x,expected):
    assert mensajeSalida(input_x) == expected