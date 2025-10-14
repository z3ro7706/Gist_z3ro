import math
def is_prime_number(x):
    if x<2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
     
        if x % i == 0:
            return False 
    return True

prime_number_list=set() #list로 받을시 탐색할때 O(n)이 되어 시간초과 발생, set을 적합하게 사용하는게 중요

for i in range(2,123456*2+1):
    if(is_prime_number(i) is True):
        prime_number_list.add(i)
    
count_list=[]
while(1):
    n=int(input())
    count=0
    if(n==0):
        break
    for i in range(n+1,2*n+1):
        if(i in prime_number_list):
            count+=1
    count_list.append(count)

for i in count_list:
    print(i)
    

