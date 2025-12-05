import sys
input = sys.stdin.readline

def BridgingtheCap(state:int, loc:int, cost:list, k:int, n:int, memo:list, vis:list):
    INF = 10**18

    if (state == 0 and loc == 1):
        return 0

    if (vis[loc][state] == 1):
        return INF

    if (memo[loc][state] != -2):
        return memo[loc][state]

    ans = INF

    if (loc == 0):
        s_list = []
        i = 0
        while (i < n):
            if (state & (1 << i)):
                s_list.append(i)
            i += 1

        m = len(s_list)
        limit = 1 << m
        sub = 1

        vis[loc][state] = 1

        while (sub < limit):
            cnt = 0
            j = 0
            while (j < m):
                if (sub & (1 << j)):
                    cnt += 1
                j += 1

            if (cnt >= 1 and cnt <= k):
                mx = -1
                j = 0
                while (j < m):
                    if (sub & (1 << j)):
                        idx = s_list[j]
                        t = cost[idx]
                        if (mx < 0 or t > mx):
                            mx = t
                    j += 1

                next_state = state
                j = 0
                while (j < m):
                    if (sub & (1 << j)):
                        p = s_list[j]
                        next_state = next_state & (~(1 << p))
                    j += 1

                nxt = BridgingtheCap(next_state, 1, cost, k, n, memo, vis)
                if (nxt >= 0 and nxt < INF and mx >= 0):
                    v = mx + nxt
                    if (v < ans):
                        ans = v

            sub += 1

        vis[loc][state] = 0

    else:
        f_list = []
        i = 0
        while (i < n):
            if (not (state & (1 << i))):
                f_list.append(i)
            i += 1

        m = len(f_list)
        limit = 1 << m
        sub = 1

        vis[loc][state] = 1

        while (sub < limit):
            cnt = 0
            j = 0
            while (j < m):
                if (sub & (1 << j)):
                    cnt += 1
                j += 1

            if (cnt >= 1 and cnt <= k):
                mx = -1
                j = 0
                while (j < m):
                    if (sub & (1 << j)):
                        idx = f_list[j]
                        t = cost[idx]
                        if (mx < 0 or t > mx):
                            mx = t
                    j += 1

                next_state = state
                j = 0
                while (j < m):
                    if (sub & (1 << j)):
                        p = f_list[j]
                        next_state = next_state | (1 << p)
                    j += 1

                nxt = BridgingtheCap(next_state, 0, cost, k, n, memo, vis)
                if (nxt >= 0 and nxt < INF and mx >= 0):
                    v = mx + nxt
                    if (v < ans):
                        ans = v

            sub += 1

        vis[loc][state] = 0

    if (ans == INF):
        ans = -1

    memo[loc][state] = ans
    return ans


data = list(map(int, input().split(',')))
n = data[0]
k = data[1]
cost = data[2:]

if (len(cost) > n):
    cost = cost[:n]

start = (1 << n) - 1
memo = [[-2] * (1 << n) for _ in range(2)]
vis = [[0] * (1 << n) for _ in range(2)]

print(BridgingtheCap(start, 0, cost, k, n, memo, vis))
