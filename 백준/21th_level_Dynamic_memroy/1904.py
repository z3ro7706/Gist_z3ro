#n번째를 처리할때는, n-1번째와  n-2번째에 블록을 추가해서 해결해야할거 같아. 
# n-1번째에는 1만 사이에 추가하면 됨, n-2번째는 00과 1,1을 사이에 추가하면 돼

import sys
input=sys.stdin.readline

binary_number_list=[0]*10000001
n=int(input())
binary_number_list[1]=1
binary_number_list[2]=2
binary_number_list[0]=0

for i in range(3,n+1):
    binary_number_list[i]=(binary_number_list[i-1]+binary_number_list[i-2])%15746

print(binary_number_list[n])


    
