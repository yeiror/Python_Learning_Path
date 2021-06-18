autor= "César Díaz,Andrés García"
autor= autor.split(",")

resultado=""
for nombre in autor:
    nombres=nombre.split()
    nombre= nombres[1]+ ","+ nombres[0]
    if len(resultado)>0:
        resultado+=";"
    resultado+= nombre
print(resultado)

    
