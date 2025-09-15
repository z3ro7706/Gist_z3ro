#진법 변환기
a, b = map(int, input().split())

def solution(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''

    while n > 0:
        n, mod = divmod(n, base)
        result += digits[mod]

    return result[::-1]

print(solution(a, b))
