#3.1.9
def contarVocales(palabra,vocales):
    resultado = []
    
    for  i in range(len(vocales)):
        plb = palabra.count(vocales[i])
        resultado.append(plb)
    return resultado

def mensajeSalida(contar,vocales):
    return "La vocal " + str(vocales[0]) + " aparece " + str(contar[0]) + "\n" + "La vocal " + str(vocales[1]) + " aparece " + str(contar[1]) + "\n" + "La vocal " + str(vocales[2]) + " aparece " + str(contar[2]) + "\n" + "La vocal " + str(vocales[3]) + " aparece " + str(contar[3]) + "\n" + "La vocal " + str(vocales[4]) + " aparece " + str(contar[4]) + "\n" 

if __name__ == "__main__":

    #entrada
    palabra = str(input("Introduzca una palabra: "))
    vocales = ["a","e","i","o","u"]

    #proceso
    contar = contarVocales(palabra,vocales)
    salida = mensajeSalida(contar,vocales)

    #salida
    print(salida)