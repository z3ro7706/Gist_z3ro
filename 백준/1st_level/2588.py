n1=int(input())
n2=int(input())
if(n1<=99 or n1>=1001 or n2<=99 or n2>=1001):
    exit(1)
    
a=n2//100
b=(n2-(100*a))//10
c=(n2-(100*a)-(10*b))

val_3 = n1 * c
val_2 = n1 * b
val_1 = n1 * a

val = val_1*100 + val_2*10 + val_3
print(val_3)
print(val_2)
print(val_1)
print(val)