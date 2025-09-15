x = int(input())  # 테스트 케이스 수

for _ in range(x):
    r, s = input().split()
    r = int(r)
    result = ""
    for char in s:
        result += char * r
    print(result)
