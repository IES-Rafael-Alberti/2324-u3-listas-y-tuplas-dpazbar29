#3.1.4
def pedirNumeros():
    numeros = []
    cont = 1
    while cont < 9:
        numero = input("Introduce el numero " + str(cont) + ": ")
        numeros.append(numero)
        cont += 1

    return numeros

def ordenarMayorMenor(numeros):
    numeros.sort()
    return numeros

if __name__ == "__main__":

    #entrada
    numeros = pedirNumeros()

    #proceso
    ordenar = ordenarMayorMenor(numeros)

    #salida
    print(ordenar)