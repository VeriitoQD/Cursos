#Harry 37.21
#Berry 37.21
#Tina 37.2
#Akriti 41
#Harsh 39
if __name__ == '__main__':
    calificaciones=[]
    totales=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        calificaciones+=[[name,score]]
        totales+=[score]
    ordenado=sorted(list(set(totales)))[1]

    for nombre,calif in sorted(calificaciones):
        if calif==ordenado:
            print(nombre)

    



