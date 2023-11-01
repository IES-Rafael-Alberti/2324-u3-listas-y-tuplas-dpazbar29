#3.1.5

def mostrar(numeros):
    '''voltea la cadena y la devuelve'''
    resultado = []
    for i in range((len(numeros)-1),-1,-1): 
        resultado.append(str(numeros[i]))
        strResultado = ",".join(resultado)
    return strResultado


if __name__ == "__main__":

    #entrada
    numeros = [1,2,3,4,5,6,7,8,9,10]

    #proceso
    salida = mostrar(numeros)

    #salida
    print(salida)