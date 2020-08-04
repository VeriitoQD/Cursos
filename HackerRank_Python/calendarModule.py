#Se recibe una fecha (MM DD YYYY) separada mediante espacios
#Hacer la busqueda del dia de la semana a la que pertenece 
#E imprimir el resultado.
#Prueba: 08 05 2015 #Salida: WEDNESDAY
import datetime
dias = ("MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY")
fecha=input().split() #Ingreso de la fecha, separando cada valor
mes=int(fecha[0])
dia=int(fecha[1])
anio=int(fecha[2])
fecha_Encontrada = datetime.date(anio,mes,dia)
semana = fecha_Encontrada.weekday()
dia_semana = dias[semana]
print("{}".format(dia_semana))