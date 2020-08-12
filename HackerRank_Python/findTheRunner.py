#5
#2 3 6 6 5
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lista=[]
    for i in arr:
        lista.append(i)
    li=sorted(set(lista),reverse=True)
    print(li[1])
        