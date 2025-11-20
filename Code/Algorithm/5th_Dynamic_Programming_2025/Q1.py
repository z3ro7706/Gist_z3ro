import sys
input = sys.stdin.readline


def Bowl(l, r, nums, dp):
    if l + 1 >= r:
        return 0

    if dp[l][r] != -1:
        return dp[l][r]

    _max = 0

    for k in range(l + 1, r):
        s = Bowl(l, k, nums, dp) + Bowl(k, r, nums, dp) + nums[l] * nums[k] * nums[r]
        if s > _max:
            _max = s

    dp[l][r] = _max
    return _max


arr = list(map(int, input().split(',')))
nums = [1] + arr + [1]
n = len(nums)
table = [[-1] * n for _ in range(n)]

print(Bowl(0, n - 1, nums, table))
