#3.1.8

def palindromo(palabra):
    '''verifica si una palabra es palindromo'''
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False
    
def mensajeSalida(verif,palabra):
    '''devuelve si es palindromo o no'''
    if verif == True:
        return "La palabra " + str(palabra) + " es palíndromo"
    if verif == False:
        return "La palabra " + str(palabra) + " no es palíndromo"

if __name__ == "__main__":

    #entrada
    palabra = input("Ingresa una palabra: ")

    #proceso
    verif = palindromo(palabra)
    salida = mensajeSalida(verif,palabra)

    #salida
    print(salida)