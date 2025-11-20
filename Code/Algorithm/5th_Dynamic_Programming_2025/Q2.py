import sys
input = sys.stdin.readline

def PlateBreaking(k, n, table):
    i = 1
    while i <= k:
        table[i][0] = 0
        table[i][1] = 1
        i += 1

    j = 0
    while j <= n:
        table[1][j] = j
        j += 1

    i = 2
    while i <= k:
        j = 2
        while j <= n:
            best = j
            x = 1
            while x <= j:
                down = table[i - 1][x - 1]
                up = table[i][j - x]

                if down > up:
                    worst = down
                else:
                    worst = up

                worst = worst + 1

                if worst < best:
                    best = worst

                x += 1

            table[i][j] = best
            j += 1
        i += 1

    return table[k][n]


k, n = map(int, input().split(','))
table = [[0] * (n + 1) for _ in range(k + 1)]

print(PlateBreaking(k, n, table))
