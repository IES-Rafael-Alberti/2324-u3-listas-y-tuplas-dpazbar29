#3.1.2

def mostrarAsignaturas(asignaturas):
    '''muestra las asignaturas de la lista'''
    resultado = []
    cont = 0
    while cont < len(asignaturas):
        resultado.append("Yo estudio " + asignaturas[cont])
        strResultado = "\n".join(resultado)
        cont += 1
    return strResultado
if __name__ == "__main__":

    #entrada
    asignaturas = ["matemáticas","física","química","historia","lengua"]
    #proceso
    mostrar = mostrarAsignaturas(asignaturas)
    #salida
    print(mostrar)