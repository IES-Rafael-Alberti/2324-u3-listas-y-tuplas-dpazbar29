#3.1.5

def mostrar(numeros):
    '''voltea la cadena y la devuelve'''
    numeros.reverse()
    resultado = ",".join(map(str,numeros))
    return resultado


if __name__ == "__main__":

    #entrada
    numeros = [1,2,3,4,5,6,7,8,9,10]

    #proceso
    salida = mostrar(numeros)

    #salida
    print(salida)