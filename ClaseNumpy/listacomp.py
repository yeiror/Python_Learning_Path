cadena="El rapido zorro marron salta sobre el perro perezoso".split()
print(cadena)
print([len(x) for x in cadena if x.lower() not in "el" ])



