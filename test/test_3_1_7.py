import pytest 
from src.E_3_1_7 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"],["b","c","e","f","h","i","k","l","n","ñ","p","q","s","t","v","w","y","z"])
    ]
)

def test_sacarLetras(input_x,expected):
    assert sacarLetras(input_x) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        (["b","c","e","f","h","i","k","l","n","ñ","p","q","s","t","v","w","y","z"],"Las letras del abecedario cuya posición no son números múltiplos de 3 son: b,c,e,f,h,i,k,l,n,ñ,p,q,s,t,v,w,y,z")
    ]
)

def test_mensajeSalida(input_x,expected):
    assert mensajeSalida(input_x) == expected