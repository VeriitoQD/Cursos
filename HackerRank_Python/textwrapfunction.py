#Separacion de cadena de acuerdo al numero ingresado
#prueba: ABCDEFGHIJKLIMNOQRSTUVWXYZ #numero: 4 
#Salida: 
###ABCD 
###EFGH 
###IJKL 
###IMNO 
###QRST 
###UVWX 
###YZ
import textwrap
#Exactamente cual es la difrencia entre wrap y fill en textwrap¿?
def wrap(string, max_width):
      #cad=textwrap.wrap(string,max_width)
      #for i in range(0,len(cad)):
        # print(cad[i]) 
      #return
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    cadena="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    #entrada=input().split()
    #cadena=entrada[0]
    #numero=entrada[1]
    numero=4
    salida=wrap(cadena,numero)
    print(salida)
