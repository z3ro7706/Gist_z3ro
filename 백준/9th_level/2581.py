import sys
input = sys.stdin.readline

def is_prime(n):
    if n <= 1:
        return 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            return 0
        i += 1
    return n

def main():
    x=int(input()) #하한
    y=int(input()) #상한

    tot=0
    min_val=0
    i=0
    while True:
        i += 1
        if i < x:
            continue
        elif i > y:
            break

        if is_prime(i):
            tot = tot + is_prime(i)
            if min_val == 0:
                min_val = is_prime(i)
    if tot == 0:
        print(-1)
    else:
        print(tot)
        print(min_val)

if __name__ == "__main__":
    main()
