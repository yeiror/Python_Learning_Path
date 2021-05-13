
def factorial(numero):
    variable=1
    for i in range(1,numero+1):
        variable*=i

    return variable

def run():
    numero=[3,4,7,1,3]
    for i in range(len(numero)):

        print(factorial(numero[i]))


if __name__== "__main__":
    run()
