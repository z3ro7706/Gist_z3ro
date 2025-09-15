tot=int(input())
num=int(input())

if(tot<=0 or tot>1000000000):
    exit(0)
    
if(num<=0 or num>100):
    exit(0)
    
add = 0

for i in range(0,num):
    p,a=map(int,input().split())
    add= add + (p*a)
    
if(add == tot):
    print("Yes")
else:
    print("No")