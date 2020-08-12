#test: input_String: abracadabra
#test: input_i_c: 5 k
#test output: abrackdabra

def mutate_string(string, position, character):
    cad=list(string)
    cad[position]=character
    string=''.join(cad)
    return string

if __name__=='__main__':
    string=input()
    i_c=input().split()
    i=int(i_c[0])
    c=i_c[1]
    print(mutate_string(string,i,c))
