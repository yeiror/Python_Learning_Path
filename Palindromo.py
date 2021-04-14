def palindromo(cadena):
   
    cadena= cadena.replace(" ","")
    cadena= cadena.lower()
    inverso = cadena[::-1]
    if inverso == cadena:
        print("Es palindromo")
    else:
        print("No es palindromo")

def run():
    cadena = input("Bienvenido, ingresa una palabra o frase para ver si es palíndromo ")
    palindromo(cadena)


if __name__ == '__main__':
    run()
