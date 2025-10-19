#연속한 수 ->n개의 연속한 수는 n-1개의 연속한 수에 1개를 더한거다
#결국 동적할당으로 값을 구해나가고, 만약 그게 max보다 크다면 max로 변환해준다.

import sys
input=sys.stdin.readline

amount=int(input())
add_list=list(map(int,input().split()))

if(len(add_list)!=amount):
    print("List input error")
    exit(0)



for i in range(1,amount):
    add_list[i]=max(add_list[i],add_list[i]+add_list[i-1])

print(max(add_list))