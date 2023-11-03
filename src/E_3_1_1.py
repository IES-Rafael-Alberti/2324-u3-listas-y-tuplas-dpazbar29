#3.1.1

def mostrarAsignaturas(asignaturas):
    '''muestra las asignaturas de la lista'''
    resultado = []
    for i in range(0,len(asignaturas)):
        resultado.append(asignaturas[i])
        strResultado = ",".join(resultado)
    return strResultado
    

if __name__ == "__main__":

    #entrada
    asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
    #proceso
    mostrar = mostrarAsignaturas(asignaturas)
    #salida
    print(mostrar)