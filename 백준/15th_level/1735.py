a,b=map(int,input().split())
c,d=map(int,input().split())

def GCD(a,b):
    while b!=0:
        a,b=b,a%b
    return a



def LCM(a,b):
    return a*b//GCD(a,b)

e=a*d+b*c #분자
f=b*d #분모

g=GCD(e,f) #둘의 최대공약수 구하기
print(e//g, f//g)