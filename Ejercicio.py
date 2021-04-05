def run():
    materias=[]
    dato=""  
    contador=0   
    print("""Programa que almacena el syllabus 
    Ingrese el nombre de las asignaturas- ingrese 0 para salir """)
    while dato != "0":
        dato =input("ingrese la materia correspondiente ")
        if dato != "0":
            materias.append(dato.replace(" ",''))
        else:
            break
    print(materias)


if __name__ == '__main__':
    run()