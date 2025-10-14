import sys
input=sys.stdin.readline

arr=input().split('-')
num=[]

for i in arr:
    sum=0
    arr_part=i.split('+')
    for j in arr_part:
        sum+=int(j)
    num.append(sum)

n=num[0]

for i in range(1,len(num)):
    n-=num[i]

print(n)