import sys
input = sys.stdin.readline

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def main():
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for num in arr:
        if is_prime(num):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
