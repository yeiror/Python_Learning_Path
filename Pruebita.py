def run():
    numero = int(input("Ingrese el tamaño de la lista en número "))
    lista=[]

    for i in range (numero):
        lista.append(int(input("Ingrese el elemento No "+ str(i+1)+ " de " + str(numero)+ " en total " )))
    
    lista.sort()
    print(lista)
    del lista
    


if __name__ == '__main__':
    run()