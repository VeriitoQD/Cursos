#9
#29
#7
#27
#output: 
def op(w,x,y,z):
    e=pow(w,x)
    f=pow(y,z)
    return e+f
if __name__=='__main__':
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    if 1<=a<=1000 and 1<=b<=1000 and 1<=c<=1000 and 1<=d<=1000:
        print(op(a,b,c,d))
    else:
        exit()
