def catalogacion_audiovisual(inventario: list) -> tuple:
    
    dvds=[x for x in inventario if x["tipo"]=="DVD"]
    cds=[x for x in inventario if x["tipo"]=="CD"]

    def eliminar_dvds(item):
        return item["tipo"]=="DVD" and item["área"]== "Tecnología" and 2021- item["año"]>15
    
    dvds_eliminados = [x["id"] for x in list(filter(eliminar_dvds,inventario))]

    def eliminar_cds(item):
        if item["tipo"]=="CD":
            if  item["área"]== "Tecnología" and 2021- item["año"]>8:
                return True
            elif 2021 - item["año"]>10:
                return True
        return False
    
    cds_eliminados = [x["id"] for x in list(filter(eliminar_cds,inventario))]
    
    permanecen= [x for x in inventario if x["id"] not in dvds_eliminados and x["id"]not in cds_eliminados]

    def ajustar_nombres(item:dict) -> dict:
        from functools import reduce
        autores = item["autor"].split(",")
        nombres= [x.split()[1]+","+x.split()[0] for x in autores ]
        item["autor"]=reduce(lambda x,y:x+";"+y, nombres)
        return item
    
    
    permanecen = list(map(ajustar_nombres,permanecen))

    return permanecen, dvds_eliminados, cds_eliminados
   
    
inventario = [
    {'id': '10', 'titulo': 'Administración de compras', 'tipo': 'CD', 'área': 'Administración', 'autor': 'César Díaz,Andrés García', 'año': 2005}, 
    {'id': '30', 'titulo': 'Actualidad matemática', 'tipo': 'CD', 'área': 'Matemáticas', 'autor': 'Pedro Navaja', 'año': 1987}, 
    {'id': '20', 'titulo': 'Fundamentos de programación', 'tipo': 'DVD', 'área': 'Tecnología', 'autor': 'César Díaz', 'año': 2001},
    {'id': '40', 'titulo': 'Actualidad informática', 'tipo': 'CD', 'área': 'Tecnología', 'autor': 'Bill Gates', 'año': 2000}, 
    {'id': '50', 'titulo': 'Atomic Physics for Dummies', 'tipo': 'CD', 'área': 'Física', 'autor': 'Albert Einstein', 'año': 1955}]        
         


print(catalogacion_audiovisual(inventario))