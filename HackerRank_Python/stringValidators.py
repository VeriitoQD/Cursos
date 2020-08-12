def validator(cad):
    cont=0
    cont2=0
    cont3=0
    cont4=0
    cont5=0
    for cadena in cad:
            if cadena.isalnum():
                cont+=1
            if cadena.isalpha():
                cont2+=1
            if cadena.isdigit():
                cont3+=1
            if cadena.islower():
                cont4+=1
            if cadena.isupper():
                cont5+=1
    if cont>0:
        print("True")
    elif cont<=0:
        print("False")
    if cont2>0:
        print("True")
    elif cont2<=0:
        print("False")
    if cont3>0:
        print("True")
    elif cont3<=0:
        print("False")
    if cont4>0:
        print("True")
    elif cont4<=0:
        print("False")
    if cont5>0:
        print("True")
    elif cont5<=0:
        print("False")

if __name__ == '__main__':
    s = input()
    if 0<len(s)<1000:
        validator(s)
    else:
        exit()