def conversor_moneda(tipo,valor):
    
    Pesos = int(input("Ingrese la cantidad de pesos " + tipo + " que desea convertir a dolares "))
    dolares = round(Pesos/valor,2)
    return(dolares)
    
menu = """ Bienvenido al Conversos de currencies
Seleccione la opción de conversion

1 - Pesos Mexicanos a Dólares
2 - Pesos Colombianos a Dólares
3 - Pesos Argentinos a Dólares
"""
while True:
        cantidad = input(menu)

        if cantidad == '1':
                print(conversor_moneda("Mexicanos", 20.86))
        elif cantidad == '2':
                print(conversor_moneda("Colombianos", 3647))
        elif cantidad == '3':
                print(conversor_moneda("Argentinos", 89.85))
        else:
                print("Ingresaste una opción incorrecta Bye")
