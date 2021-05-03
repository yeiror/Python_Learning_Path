def run():
    lista=[8, 10, 6, 2, 4]
    swapped=True
    while swapped:
        swapped=False
        for i in range(len(lista)-1):
            if(lista[i]>lista[i+1]):
                lista[i], lista[i+1]= lista[i+1], lista[i]
                swapped=True
        
    print(lista)




if __name__== "__main__":
    run()