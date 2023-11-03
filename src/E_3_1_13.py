#3.1.13

def pedirNumeros():
    numeros = []
    a = True
    while a == True:
        numero = input("Introduzca un número (introduzca 'a' para terminar): ")
        try:
                numeros.append(int(numero))
        except ValueError:
                print("Por favor, introduzca un número válido o 'a' para terminar.")

        if numero.lower() == "a":
            a = False
    return numeros

def media(numeros):
    return sum(numeros)/len(numeros)

def desvicionTipica(numeros):
    media_aritmetica = media(numeros)
    suma = 0

    for i in range(len(numeros)):
        suma += (numeros[i]-media_aritmetica)**2
    desviacion = (suma/len(numeros))**0.5

    return round(desviacion,2)


def mensajeSalida(numeros,result_media,result_desviacion):
     return "La media de " + str(sum(numeros)) + " es: " + str(result_media) + " y la desviación típica es: " + str(result_desviacion)



if __name__ == "__main__":

    #entrada
    numeros = pedirNumeros()

    #proceso
    result_media = media(numeros) 
    result_desviacion = desvicionTipica(numeros)
    salida = mensajeSalida(numeros,result_media,result_desviacion)

    #salida
    print(salida)