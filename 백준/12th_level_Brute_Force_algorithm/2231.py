def Digit_Generator(x:int):
    y=list(str(x))
    count=0
    for i in y:
        count=count+int(i)
    
    return count

x=int(input())
arr=[]
for i in range(1,x+1):
    a= Digit_Generator(x-i)
    if(a==i):
        arr.append(x-i)

if(len(arr)!=0):
    print(min(arr))
else:
    print("0")
    
