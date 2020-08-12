def swap_case(s):
    cad=''
    for i in s:
        if i.isupper():
            cad=cad+i.lower()
        elif i.islower():
            cad=cad+i.upper()
        else:
            cad=cad+i
    return cad

if __name__ == "__main__":
    pass
cadena=input()
stringc=swap_case(cadena)
print(stringc)