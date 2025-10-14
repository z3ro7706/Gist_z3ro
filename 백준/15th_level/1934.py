x=1

def GCD(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def LCM(a,b):
    return a*b//GCD(a,b)

arr=[]

for i in range(0,x):
    a,b=map(int,input().split())
    arr.append(LCM(a,b))

for i in arr:
    print(i)