# Merge Sort, Time complexity = O(n log n)
def make_list():  # 사용할 리스트 반환
    x = int(input())  # 받을 데이터 개수
    arr = []  # 받은 숫자 리스트
    for i in range(0, x):
        a = int(input())
        arr.append(a)
    return arr  

def Two_list(i: list, j: list):
    arr = []
    a = 0
    b = 0
    while a < len(i) and b < len(j):
        if i[a] < j[b]:
            arr.append(i[a])
            a += 1
        else:
            arr.append(j[b])
            b += 1
    arr += i[a:]
    arr += j[b:]
    return arr

def Merge_sort(l: list):
    length = len(l)  # 리스트 개수
    if length <= 1:
        return l
    mid = length // 2
    left_half = Merge_sort(l[:mid])
    right_half = Merge_sort(l[mid:])
    return Two_list(left_half, right_half)

List = make_list()
Sort = Merge_sort(List)
for i in Sort:
    print(i)
