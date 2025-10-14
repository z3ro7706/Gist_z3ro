import sys
input=sys.stdin.readline


l=int(input())

p_n=[0]*101
p_n[1]=1
p_n[2]=1
p_n[3]=1
p_n[4]=2
p_n[5]=2
p_n[6]=3


for i in range(0,l):
    n=int(input())
    for i in range(7,n+1):
        p_n[i]=p_n[i-1]+p_n[i-5]
    print(p_n[n])
