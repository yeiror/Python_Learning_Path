import math

def camas_a_mover(camas_actual, ocupacion_actual, ocupacion_esperada = 70):
    """Función que indica el déficit de camas en el municipio"""
    if(ocupacion_actual>=ocupacion_esperada):
        camas_ocupadas=math.ceil((ocupacion_actual*camas_actual)/100)
        camas_esperadas=((camas_ocupadas*100)/ocupacion_esperada)-camas_actual
        return math.ceil(camas_esperadas)
    else:
        return("La ocupación actual es menor al 90%, no hay necesidad de trasladar camas")

print(camas_a_mover(350,100,1))
