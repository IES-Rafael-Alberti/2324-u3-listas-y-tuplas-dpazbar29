#3.1.10

def maximo(numeros):
    maxi = max(numeros)
    return maxi

def minimo(numeros):
    mini = min(numeros)
    return mini

def mensajeSalida(max,min):
    return "El maximo es: " + str(max) + "\nEl minimo es: " + str(min)


if __name__ == "__main__":

    #entrada
    numeros = [50, 75, 46, 22, 80, 65, 8]

    #proceso
    maxi = maximo(numeros)
    mini = minimo(numeros)
    salida = mensajeSalida(maxi,mini)

    #salida
    print(salida)