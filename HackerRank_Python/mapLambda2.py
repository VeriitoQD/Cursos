cube = lambda x: pow(x,3)# complete the lambda function 
def fibonacci(n):
    lista=[]
    a=0
    b=1
    for i in range(n):
        lista.append(a)
        a,b=b,a+b
    return lista

if __name__=='__main__':
    n=int(input())
    print(fibonacci(n))
