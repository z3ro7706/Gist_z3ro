import sys
input = sys.stdin.readline

def max_profit(cost:list):
    n = len(cost)
    if(n<=1):
        return 0

    dp = [0] * n

    for i in range(1, n):
        best = 0
        for k in range(i):
            profit = dp[k]+ (cost[i]-cost[k])
            if(profit>best):
                best=profit

        if(dp[i - 1]>best):
            dp[i] = dp[i-1]
        else:
            dp[i] = best

    return dp[n-1]


x = list(map(int, input().split(',')))

print(max_profit(x))
