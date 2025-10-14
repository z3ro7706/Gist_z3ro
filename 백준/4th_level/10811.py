x,y = map(int, input().split())

arr = []
for i in range(0,x):
    arr.append(i+1)

for i in range(0,y):
    s1,s2=map(int, input().split())
    arr[s1-1:s2] = arr[s1-1:s2][::-1]

print(*arr)