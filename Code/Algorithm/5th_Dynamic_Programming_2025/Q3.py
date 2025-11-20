import sys
input = sys.stdin.readline


def LCS(n, m, A, B, table):
    if n == 0 or m == 0:
        return 0
    
    if table[n][m] != -1:
        return table[n][m]
    
    if A[n - 1] == B[m - 1]:
        table[n][m] = LCS(n - 1, m - 1, A, B, table) + 1
    else:
        val1 = LCS(n - 1, m, A, B, table)
        val2 = LCS(n, m - 1, A, B, table)
        table[n][m] = _max(val1, val2)
    return table[n][m]


def _max(a, b):
    if a >= b:
        return a
    return b


A,B=map(list,input().split(','))


table = [[-1] * (len(B) + 1) for _ in range(len(A) + 1)]

print(LCS(len(A), len(B), A, B, table))
