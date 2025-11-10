import sys
input = sys.stdin.readline

# (abs(x), x) 기준으로 x가 y보다 "작은가?"
def is_less(x, y):
    ax, ay = abs(x), abs(y)
    if ax != ay:
        return ax < ay
    return x < y  # 절댓값 같으면 실제 값 작은 쪽(음수 우선)

def Make_heap(arr: list):
    if len(arr) <= 1:
        return arr
    arr_heap = []
    arr_heap.append(arr[0])
    for i in range(1, len(arr)):
        arr_heap = Heap_append(arr_heap, arr[i])
    return arr_heap

def Heap_append(arr: list, n: int):
    if len(arr) < 1:
        arr.append(n)
        return arr
    arr.append(n)
    point = len(arr) - 1
    # up-heap: 자식이 부모보다 "작으면" 올라간다.
    while point > 0:
        parent = (point - 1) // 2
        if is_less(arr[point], arr[parent]):
            arr[point], arr[parent] = arr[parent], arr[point]
            point = parent
        else:
            break
    return arr

def Delete_min_heap(arr: list):
    # 빈 경우는 바깥에서 처리하므로 여기선 최소 1개 가정
    if len(arr) == 1:
        v = arr.pop()
        print(v)
        return arr

    # 루트 값을 꺼내 출력하고, 마지막 원소를 루트로 올린 뒤 down-heap
    v = arr[0]
    arr[0] = arr.pop()
    print(v)

    point = 0
    n = len(arr)

    while True:
        left = 2 * point + 1
        right = 2 * point + 2
        smallest = point

        if left < n and is_less(arr[left], arr[smallest]):
            smallest = left
        if right < n and is_less(arr[right], arr[smallest]):
            smallest = right

        if smallest != point:
            arr[point], arr[smallest] = arr[smallest], arr[point]
            point = smallest
        else:
            break

    return arr

x = int(input().strip())
arr = []
for _ in range(x):
    data = int(input())
    if data == 0:
        if len(arr) == 0:
            print(0)
        else:
            arr = Delete_min_heap(arr)
    else:
        if len(arr) == 0:
            arr.append(data)
        else:
            arr = Heap_append(arr, data)
