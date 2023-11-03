#3.1.4
def pedirNumeros():
    '''pide los números de la primitiva'''
    numeros = []
    cont = 1
    while cont < 9:
        numero = int(input("Introduce el numero " + str(cont) + ": "))
        numeros.append(numero)
        cont += 1

    return numeros

def ordenarMayorMenor(numeros):
    '''ordena los numeros de mayor a menor'''
    numeros.sort()
    return numeros

if __name__ == "__main__":

    #entrada
    numeros = pedirNumeros()

    #proceso
    ordenar = ordenarMayorMenor(numeros)

    #salida
    print(ordenar)