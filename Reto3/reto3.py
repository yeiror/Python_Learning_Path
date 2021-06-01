def simulador_prestamo_baniscutp(datos_prestamo: dict) -> dict:
    TMV=((1+(datos_prestamo["interes anual"]/100))**(1/12))-1
    saldo_a_financiar= datos_prestamo["prestamo"]+datos_prestamo["gastos documentacion"]
    cuota=round((saldo_a_financiar)/((1-((1+TMV)**(-datos_prestamo["cuotas"])))/TMV),0)
    cuotafija=cuota
    nuevo_Saldo=saldo_a_financiar
    amortizacion=[]
    for i in range(datos_prestamo["cuotas"]):
       valor_interes = round(nuevo_Saldo * TMV,2) 
       if i+1 == datos_prestamo["cuotas"]:
           cuota= round((nuevo_Saldo + valor_interes),2)
       capital_abonado = round(cuota - valor_interes,2)
       nuevo_Saldo=round(nuevo_Saldo-capital_abonado,2)
       amortizacion.append((i+1,capital_abonado,valor_interes,cuota,nuevo_Saldo))
       valor_interes=round(nuevo_Saldo*TMV,2)
    
    return{
        "saldo financiar": saldo_a_financiar,
        "cuota": cuotafija,
        "amortizacion": amortizacion
    }
diccionario={
    "prestamo": 2000000.0,
    "gastos documentacion": 0.0,
    "cuotas": 6,
    "interes anual": 28.99
    }

print(simulador_prestamo_baniscutp(diccionario))