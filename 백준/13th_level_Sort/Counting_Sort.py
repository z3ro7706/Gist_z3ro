#Counting Sort(중복된 값이 많이 분포되어 있을 때 & 최대, 최소 차이가 100만 이하)
x=int(input()) #받을 데이터의 개수 
if(x==0):
    exit(0)

if(x<=0 or x>10000000):
    exit(0)

arr=[]
for i in range(0,10001): #0으로 찬 배열 생성
    arr.append(0)

for i in range(0,x):
    y=int(input())
    arr[y]+=1

for i in range(len(arr)):
    for j in range(0,arr[i]):
        print(i)