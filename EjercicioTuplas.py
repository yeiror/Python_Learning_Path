def run():
   print("Programa para corregir las fechas dadas un horario del evento")
   horas=int(input("Ingresa la hora que inició evento "))
   minutos= int(input("Ingresa los minutos de inicio del evento "))
   dura= int(input("Ingresa la duración del evento"))

   #Encontrar el total de minutos
   minutos+=dura

   #Encontrar el número de horas ocultas en los minutos
   #Si es mayor de sesenta sumará 
   horas+= minutos//60

   #Corregir los minutos para que estén en un rango de 60
   minutos = minutos % 60

   #Corregir las horas para que estén en un rango de 60
   horas= horas % 24

   print(horas, ":", minutos, sep="")

if __name__=="__main__":
    run()