#Se recibe una fecha (MM DD YYYY) separada mediante espacios
#Hacer la busqueda del dia de la semana a la que pertenece 
#E imprimir el resultado.
#Prueba: 08 05 2015 #Salida: WEDNESDAY
#Ingreso de la fecha, separando cada valor

# import Python's datetime module
import datetime
# weekdays as a tuple
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
# Find out what day of the week is this year's Christmas
fecha=input().split()
mes=int(fecha[0])
dia=int(fecha[1])
anio=int(fecha[2])
thisXMas    = datetime.date(anio,mes,dia)
thisXMasDay = thisXMas.weekday()
thisXMasDayAsString = weekDays[thisXMasDay]
print("This year's Christmas is on a {}".format(thisXMasDayAsString))