import sys

while (True):
    li = list(map(int, sys.stdin.readline().split()))
    if (sum(li) == 0):
        break

    n = li[0]

    MAX = 0
    stack = []
    for i, h in enumerate(li):
        if (i == 0):
            continue

        if stack and (stack[-1][1] > h):
            while (stack):
                idx, height = stack.pop()
                width = 1
                if (stack):
                    width = stack[-1][0] + 1

                result = (i - width) * height
                MAX = max(result, MAX)

                if (not stack) or (stack[-1][1] <= h):
                    break
            

        if (not stack) or (stack[-1][1] <= h):
            stack.append((i, h))

    while (stack):
        idx, height = stack.pop()
        width = 1
        if (stack):
            width = stack[-1][0] + 1

        result = (n + 1 - width) * height
        MAX = max(result, MAX)

    print(MAX)