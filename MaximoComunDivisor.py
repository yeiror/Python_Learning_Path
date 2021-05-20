def mcd(x,y):
    if y < 0:
        return "No puede buscar divisores si hay números negativos"

    # Algoritmo
    if y == 0:
        return x
    if x >= y:
        return mcd(y, x % y) 
    else:
        return mcd(y, x)

def run():
    print(mcd(24,12))
    
if __name__=="__main__":
    run()