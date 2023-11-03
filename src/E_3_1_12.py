#3.1.12


def productoMatrices(matriz_a,matriz_b):
    resultado = [[0,0],[0,0]]
    for i in range(len(matriz_a)):
            for j in range(len(matriz_b[0])):
                for k in range(len(matriz_b)):
                    resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
    return resultado


def mensajeSalida(resultado):
     
    return "El resultado es: " + str(resultado)

if __name__ == "__main__":

    #entrada
    matriz_a = [[1,2,3],[4,5,6]]
    matriz_b = [[-1,0],[0,1],[1,1]]

    #proceso
    resultado = productoMatrices(matriz_a,matriz_b)
    matriz_final = mensajeSalida(resultado)

    #salida
    print(resultado)
    print(matriz_final)