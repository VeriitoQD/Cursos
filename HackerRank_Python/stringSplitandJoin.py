def split_and_join(line):
    # write your code here
    line=line.split(" ")
    line="-".join(line)
    return line
    
if __name__ == "__main__":
    cadena=input()
    cad=split_and_join(cadena)
    pass

