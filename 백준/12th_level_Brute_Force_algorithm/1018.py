n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

min_count = 64  # 8x8 최대 칠해야 하는 수

for i in range(n - 7):
    for j in range(m - 7):
        count1 = 0  # 시작이 'W'
        count2 = 0  # 시작이 'B'

        for x in range(8):
            for y in range(8):
                current = board[i + x][j + y]
                if (x + y) % 2 == 0:
                    if current != 'W':
                        count1 += 1
                    if current != 'B':
                        count2 += 1
                else:
                    if current != 'B':
                        count1 += 1
                    if current != 'W':
                        count2 += 1
        min_count = min(min_count, count1, count2)

print(min_count)
