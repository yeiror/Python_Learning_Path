def Cantidad_de_plantas(CadenaLugar:str, CadenaCultivo:str, LargoTerreno:float, AnchoTerreno:float, LargoCultivo:float, AnchoCultivo:float ):
    """Función para calcular cuantas plantas de un cultivo dado se pueden sembrar en un terreno
    """
    Ncultivos=int((LargoTerreno*AnchoTerreno)/(LargoCultivo*AnchoCultivo))
    return (f"En {CadenaLugar} se pueden plantar {Ncultivos} de {CadenaCultivo}")

print(Cantidad_de_plantas("Chía","Remolachas",6,6,2,2))
