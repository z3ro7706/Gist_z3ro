a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if c < a1:
    print(0)
elif c == a1:
    print(1 if a0 <= 0 else 0)
else:
    print(1 if (c - a1) * n0 >= a0 else 0)
