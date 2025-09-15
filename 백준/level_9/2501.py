x,y=map(int,input().split()) #x : 숫자, y : 순서
arr=[]
for i in range(1,x+1):
    if(x%i==0):
        arr.append(i)
if(y>len(arr)):
    print("0")
    exit(0)
print(arr[y-1])