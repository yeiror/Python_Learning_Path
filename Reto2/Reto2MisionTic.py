def calculo_recargos(cliente: dict) -> dict:
    """ Calcula el porcentaje de recargo a aplicar en cada tipo de producto"""
    if cliente["nacional"]==True:
        del(cliente["nacional"])
        compratotal=cliente["agujas"]+cliente["escolares"]+cliente["hogar"]

        if(compratotal>=200000000):
            cliente["agujas"],cliente["escolares"],cliente["hogar"]=10.0,10.0,10.0

        elif(cliente["agujas"]>70000000 and cliente["escolares"]>30000000 and cliente["hogar"]>40000000):
            cliente["agujas"],cliente["escolares"],cliente["hogar"]=7.0,7.0,7.0
        else:
            if(cliente["agujas"]>70000000):
                cliente["agujas"]=5.0
            else:
                cliente["agujas"]=0.0
            if(cliente["escolares"]>30000000):
                cliente["escolares"]=5.0
            else:
                cliente["escolares"]=0.0
            if(cliente["hogar"]>40000000):
                cliente["hogar"]=5.0
            else:
                cliente["hogar"]=0.0
        return cliente
    
    else:
        
        del(cliente["nacional"])
        compratotal=cliente["agujas"]+cliente["escolares"]+cliente["hogar"]

        if(compratotal>=100000):
            cliente["agujas"],cliente["escolares"],cliente["hogar"]=8.0,8.0,8.0

        elif(cliente["agujas"]>25000 and cliente["escolares"]>10000 and cliente["hogar"]>15000):
            cliente["agujas"],cliente["escolares"],cliente["hogar"]=5.0,5.0,5.0
        else:
            if(cliente["agujas"]>25000):
                cliente["agujas"]=3.0
            else:
                cliente["agujas"]=0.0
            if(cliente["escolares"]>10000):
                cliente["escolares"]=3.0
            else:
                cliente["escolares"]=0.0
            if(cliente["hogar"]>15000):
                cliente["hogar"]=3.0
            else:
                cliente["hogar"]=0.0
        return cliente

def run():
    dict={
        "nombre" : "César Díaz",
        "nacional": True,
        "agujas": 150000000.0,
        "escolares": 30000000.0,
        "hogar": 20000000.0
        }
    
    print(calculo_recargos(dict))

if __name__=="__main__":
    run()
