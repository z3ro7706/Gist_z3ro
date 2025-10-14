import sys
from collections import deque
input = sys.stdin.readline

N = int(input())  # 자료구조의 수
A = list(map(int, input().split()))  # 자료구조 종류 (0=큐, 1=스택)
B = list(map(int, input().split()))  # 초기값
M = int(input())  # 삽입할 수열 길이
C = list(map(int, input().split()))  # 삽입할 값들

dq = deque()
# 큐인 자료구조의 초기값을 역순으로 front에 넣음
for i in range(N-1, -1, -1):
    if A[i] == 0:
        dq.appendleft(B[i])

# 이후 삽입 & pop 반복
result = []
for x in C:
    dq.appendleft(x)
    result.append(dq.pop())

print(*result)
