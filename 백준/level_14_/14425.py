n, m = map(int, input().split())
List_s = set()

for i in range(0,n):
    List_s.add(input())

count = 0
 
for i in range(0,m):
    word = input()
    if word in List_s:
        count += 1

print(count)
