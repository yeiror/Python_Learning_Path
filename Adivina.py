import random

def Adivinadora(numero):
    choice = int(input("Adivina el número entre 0 - 100 "))
    while True:
        if choice == numero:
            print("El número "+ str(choice)+ " es correcto")
            break
        elif choice > numero:
            choice = int(input("Menos "))
        else:
            choice = int(input("Más "))
           

def run():

    variable = random.randrange(100)
    Adivinadora(variable)
   

if __name__ == '__main__':
    run()