import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = 0
mod_count = [0] * b  # 나머지별 등장 횟수
mod_count[0] = 1     # 누적합 자체가 b로 나누어 떨어지는 경우

count = 0
for num in arr:
    prefix_sum += num
    remainder = prefix_sum % b
    count += mod_count[remainder]  # 같은 나머지 개수만큼 새로운 구간이 성립
    mod_count[remainder] += 1

print(count)
