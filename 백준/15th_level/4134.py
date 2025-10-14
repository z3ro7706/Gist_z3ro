x=int(input()) #amount of case


import math

def is_prime_number(x):
    if x<2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
     
        if x % i == 0:
            return False 
    return True


arr=[]
for x in range(0,x):
    n=int(input())
    while(1):
        if(is_prime_number(n) is True):
            arr.append(n)
            break
        else:
             n+=1


for i in arr:
    print(i)
        