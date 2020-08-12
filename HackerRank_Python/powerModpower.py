def calculatepow2(x,y):
    return pow(x,y)

def calculatepow3(x,y,z):
    return pow(x,y,z)

if __name__=='__main__':
    a=int(input())
    b=int(input())
    m=int(input())
    if 1<=a<=10 and 1<=b<=10 and 2<=m<1000:
        print(calculatepow2(a,b))
        print(calculatepow3(a,b,m))
    else:
        exit()


