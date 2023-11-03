#3.1.8

def palindromo(palabra):
    '''verifica si una palabra es palindromo'''
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]

    return palabra == palabra_invertida
    
def mensajeSalidaSi(verif):
    '''devuelve si es palindromo o no'''
    if verif == True:
        return "La palabra es palíndromo"

def mensajeSalidaNo(verif):
    if verif == False:
        return "La palabra no es palíndromo"
    

if __name__ == "__main__":

    #entrada
    palabra = input("Ingresa una palabra: ")

    #proceso
    verif = palindromo(palabra)
    salida_si = mensajeSalidaSi(verif)
    salida_no = mensajeSalidaNo(verif)

    #salida
    if verif == True:
        print(salida_si)
    else:
        print(salida_no)