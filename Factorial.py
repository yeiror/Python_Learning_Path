
def factorial(numero):
    if(numero==1 or numero==0):
        return 1
    else:
        return numero * factorial(numero-1)

def run():
    numero=[3,4,7,1,3]
    for i in range(len(numero)):
        print(factorial(numero[i]))

if __name__== "__main__":
    run()
