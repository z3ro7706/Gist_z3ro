n,v = map(int, input().split())
n_list = list(map(int, input().split()))
arr=[]

count = 0

for i in n_list:
    if i<v:
        arr.append(i)

print(*arr)
