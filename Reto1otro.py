def promedio_precios(BMW:int,Ducati:int,Honda: int,Kawasaki: int, KTM):
    promedio= round((((BMW+Ducati+KTM)*4300)+((Honda+Kawasaki)*3600))/5,2)
    return(f"El promedio de precio de una moto sport touring es: {promedio} pesos colombianos")

print(promedio_precios(BMW=32500,Ducati=31000,Honda=24000,Kawasaki=25500,KTM=30800))
