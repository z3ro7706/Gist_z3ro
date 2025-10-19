x,y=map(int,input().split())

value=1
for i in range(0,y):
    value=value*x
    x-=1
    
   

for i in range(1,y+1):
    value=value//i
 

print(value)