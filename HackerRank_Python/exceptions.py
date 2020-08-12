N=int(input())
if 0<N<10:
    a=[]
    b=[]
    for i in range(N):
        cad=input().split()
        a.insert(i,cad[0])
        b.insert(i,cad[1])
    for i in range(N):
        try:
            print(int(round(int(a[i])/int(b[i]))))
        except ZeroDivisionError as error:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code:", e)
else:
    exit()