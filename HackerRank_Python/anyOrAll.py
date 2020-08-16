#5
#12 9 61 5 14
#True
#Condition 1: All the integers in the list are positive.
#Condition 2: 5 is a palindromic integer.
#Can you solve this challenge in 3 lines of code or less?
#There is no penalty for solutions that are correct but have more than 3 lines.
N,lista=int(input()),input().split()
print(all([int(i)>0 for i in lista]) and any([str(i)==str(i)[::-1] for i in lista]))
