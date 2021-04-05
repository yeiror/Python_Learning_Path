def esPrimo(numero):
    contador=0
    for i in range(1, numero+1):
        if i==1 or i==numero:
            continue
        elif numero % i == 0:
            contador+=1

    if contador > 0:
        return False
    else:
        return True


def run():
    numero = int(input("Ingrese un número para verificar si es primo o no: "))
    if esPrimo(numero):
        print("El número "+ str(numero) + " es primo")
    else:
        print("El número "+ str(numero) + " no es primo")


if __name__ == '__main__':
    run()