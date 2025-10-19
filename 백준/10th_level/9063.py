x=int(input()) #총 리스트 개수

arr_x=[]
arr_y=[]
for i in range(0,x):
    a,b=map(int,input().split())
    arr_x.append(a)
    arr_y.append(b)
    if(x==1):
        print("0")
        exit(0)
    
i=max(arr_x)
j=min(arr_x)
k=max(arr_y)
l=min(arr_y)
print((i-j)*(k-l))
