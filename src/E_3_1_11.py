#3.1.11

def calculoProductoEscalar(vector_u,vector_v):
    temporal = []
    for i in range(len(vector_u)):
        temporal.append(vector_u[i]*vector_v[i])
    resultado = sum(temporal)
    return resultado 

def mensajeSalida(vector_u,vector_v,escalar):
    return "El resultado del producto escalar de: " + str(vector_u) + " + " + str(vector_v) + " = " + str(escalar) 


    
    
if __name__ == "__main__":

    #entrada
    vector_u = [1,2,3]
    vector_v = [-1,0,2]

    #proceso
    escalar = calculoProductoEscalar(vector_u,vector_v)
    salida = mensajeSalida(vector_u,vector_v,escalar)

    #salida
    print(salida)