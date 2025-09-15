#d'Ocange's identity(도가뉴 항등식)을 이요한 풀이 방식) : 짝수번째와 홀수 번쨰의 특징을 이용해서 빠르 게 탐색한다.(데이터 양이 감소하여서 DP로 문제를 해결)
#메모리 용량이 타이트 하므로 pypy3로는 불가능함, 따라서 Python으로 풀어야 메모리 초과가 발생하지 않음

import sys
sys.setrecursionlimit(10**8)
memo = {}
memo[0] = 0
memo[1] = 1
memo[2] = 1

def dp(i):
    if i not in memo:
        if i%2==0:
            memo[i] = (dp(i//2) * (dp(i//2) + 2*dp(i//2-1)))%1000000007
        else:
            memo[i] = (dp(i//2)**2 + dp(i//2+1)**2)%1000_000007
    return memo[i]

n = int(input())
print(dp(n))