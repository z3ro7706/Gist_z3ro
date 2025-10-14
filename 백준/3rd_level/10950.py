x=int(input())
num = []
for i in range(0,x):
    n1,n2=map(int,input().split())
    num.append(n1+n2)
    
for i in range(0,x):
    print(num[i])