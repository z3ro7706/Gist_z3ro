import sys

N = int(sys.stdin.readline())

arr = [-1] * (N+2) #array를 -1로 채움, 이때 갯수를 N+2로 넉넉하게 잡아주기 (피보나치수가 들어갔는지 확인하기 위해서 )
arr[1] = 1
arr[0] = 0
def fib(i):
    if arr[i] != -1 : #만약 arr[i]번째 칸이 -1이 아니면 되돌려주기 (이미 피보나치 수열이 들어가 있는거임) : 오류방지
        return arr[i]
    else:
        arr[i] = fib(i-2) + fib(i-1) #전 2개의 피보나치를 호출, 이때 fib가 아니라 arr로 호출하면 계산이 진행이 안됫을 경우가 생겨 오류 발생 가능성 생김
        return arr[i]

print(fib(N))

#O(n)=2^n in fibonacci coursion