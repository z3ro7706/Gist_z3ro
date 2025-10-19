import sys
input=sys.stdin.readline

x=int(input())
arr=[]
count=0
end=0
for i in range(x):
    a,b=map(int,input().split())
    arr.append([a,b])

arr.sort(key=lambda x: (x[1], x[0])) #2차원 배열

for i in range(x):
    if(arr[i][0]>=end):
        end=arr[i][1]
        count+=1
        

print(count)