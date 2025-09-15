import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 너무 크게 잡지 않기

def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global cnt, res, tmp

    i, j = p, q + 1
    t = p

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1

    while i <= q:
        tmp[t] = A[i]
        i += 1
        t += 1

    while j <= r:
        tmp[t] = A[j]
        j += 1
        t += 1

    for i in range(p, r + 1):
        A[i] = tmp[i]
        cnt += 1
        if cnt == K:
            res = A[i]

# 입력
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 전역 변수 및 전처리
cnt = 0
res = -1
tmp = [0] * N  # 메모리 절약용 전역 임시 배열

# 실행
mergeSort(A, 0, N - 1)
print(res)
