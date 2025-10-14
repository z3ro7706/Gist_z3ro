x,y=map(int,input().split())
if(x<=0 or x>100 or y<0 or y>100):
    exit(0)

arr=[]
for i in range(0,x):
    arr.append(i+1) #1,2,3,4... 리스트 생성

for i in range(0,y):
    n1, n2=map(int,input().split())
    arr[n1-1], arr[n2-1] = arr[n2-1], arr[n1-1]

print(*arr)