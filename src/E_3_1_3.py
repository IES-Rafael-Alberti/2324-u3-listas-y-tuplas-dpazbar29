#3.1.3


def mostrarAsignaturasNotas(asignaturas):
    '''pide las notas de cada asiantura'''
    notas = []
    cont = 0

    while cont < len(asignaturas):
        nota = input("Introduce la nota de " + str(asignaturas[cont]) + ": ")
        notas.append(nota)
        cont += 1
    return notas

def mensajeSalida(asignaturas,notas):
    '''muestra la nota de cada asignatura'''
    resultado = []
    cont = 0
    while cont < len(asignaturas):
        resultado.append("En " + asignaturas[cont] + " has sacado un " + str(notas[cont]))
        strResultado = "\n".join(resultado)
        cont += 1
    return strResultado

if __name__ == "__main__":

    #entrada
    asignaturas = ["matemáticas","física","química","historia","lengua"]
    
    #proceso
    notas = mostrarAsignaturasNotas(asignaturas)
    salida = mensajeSalida(asignaturas,notas)

    #salida
    print(salida)
