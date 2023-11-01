#3.1.6

def pedirNotas(asignaturas):
    '''pide las notas de cada asiantura'''
    notas = []
    cont = 0

    while cont < len(asignaturas):
        nota = int(input("Introduce la nota de " + str(asignaturas[cont]) + ": "))
        notas.append(nota)
        cont += 1
    return notas

def asignaturasSuspensas(asignaturas,notas):
    '''devuelve las asignaturas suspensas'''
    suspensas = []
    cont = 0
    while cont < len(asignaturas):
        if notas[cont] < 5:
            suspensas.append(asignaturas[cont])
        cont += 1
    return suspensas

def mensajeSalida(suspensas):
    '''muestra las asignaturas a repetir'''
    resultado = []
    cont = 0
    while cont < len(suspensas):
        resultado.append("Tienes que repetir " + str(suspensas[cont]))
        strResultado = "\n".join(resultado)
        cont += 1
    return strResultado 

if __name__ == "__main__":

    #entrada
    asignaturas = ["matemáticas","física","química","historia","lengua"]
    
    #proceso
    notas = pedirNotas(asignaturas)
    suspensas = asignaturasSuspensas(asignaturas,notas)
    salida = mensajeSalida(suspensas)

    #salida
    print(salida)
