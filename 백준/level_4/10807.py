n = int(input())
n_list = list(map(int, input().split()))
v = int(input())

count = 0
for i in n_list:
    if i == v:
        count += 1

print(count)
