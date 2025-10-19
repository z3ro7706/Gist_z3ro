import sys
input=sys.stdin.readline

from collections import deque

n = int(input())
values = list(map(int, input().split()))

balloons = deque((i + 1, v) for i, v in enumerate(values))  # (풍선번호, 이동값)
result = []

while balloons:
    index, move = balloons.popleft()
    result.append(index)
    if move > 0:
        balloons.rotate(-(move - 1))  # 양수면 왼쪽으로 회전
    elif move < 0:
        balloons.rotate(-move)  # 음수면 오른쪽으로 회전

print(*result)
