import sys
input = sys.stdin.read

lines = input().strip().split('\n')
n = int(lines[0])
points = [tuple(map(int, line.split())) for line in lines[1:]]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        # y 오름차순, 같으면 x 오름차순
        if left[i][1] < right[j][1] or (left[i][1] == right[j][1] and left[i][0] <= right[j][0]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

sorted_points = merge_sort(points)

for x, y in sorted_points:
    print(x, y)
