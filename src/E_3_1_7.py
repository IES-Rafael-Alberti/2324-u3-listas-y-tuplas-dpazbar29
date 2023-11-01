#3.1.7


def sacarLetras(abecedario):
    '''elimina las letras con posicion multiplo de 3'''
    cont = 1
    while cont < len(abecedario):
        if cont % 3 == 0:
            del abecedario[cont - 1]
        cont += 1
    return abecedario

def mensajeSalida(letras):
    '''muestras las letras con posicion no multiplo de 3'''
    strResultado = ",".join(letras)
    return "Las letras del abecedario cuya posición no son números múltiplos de 3 son: " + strResultado


if __name__ == "__main__":

    #entrada
    abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

    #proceso
    letras = sacarLetras(abecedario)
    salida = mensajeSalida(letras)

    #salida
    print(salida)