import math
def is_prime_number(x):
    if x<2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
     
        if x % i == 0:
            return False 
    return True

prime_number_list=set()
for i in range(2,1000001):
    if(is_prime_number(i) is True):
        prime_number_list.add(i)

x=int(input())
arr=[]
for i in range(0,x):
    y=int(input())
    count=0
    for j in range(2,y//2+1):
        if(j in prime_number_list):
            if((y-j) in prime_number_list):
                count+=1
    arr.append(count)

for i in arr:
    print(i)