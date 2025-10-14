N = int(input())

for i in range(1, N + 1):
    stars = '*' * (2 * i - 1)
    spaces = ' ' * (N - i)
    print(spaces + stars)

for i in range(N - 1, 0, -1):
    stars = '*' * (2 * i - 1)
    spaces = ' ' * (N - i)
    print(spaces + stars)
