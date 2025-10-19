arr=[1,1,2,2,2,8]
con=list(input().split())

for i in range(0,6):
    arr[i] = arr[i] - int(con[i])

print(*arr)