import sys
from collections import Counter

def mean(value: list):
    print(round(sum(value) / len(value)))

def middle(value: list):
    value.sort()
    print(value[len(value) // 2])

def mode(value: list):
    counter = Counter(value)
    freq_list = counter.most_common()
    max_freq = freq_list[0][1]
    mode_candidates = [num for num, freq in freq_list if freq == max_freq]
    mode_candidates.sort()
    print(mode_candidates[1] if len(mode_candidates) > 1 else mode_candidates[0])

def different(value: list):
    print(max(value) - min(value))

input = sys.stdin.readline
x = int(input())
arr = []
for _ in range(x):
    arr.append(int(input()))

mean(arr)
middle(arr)
mode(arr)
different(arr)
