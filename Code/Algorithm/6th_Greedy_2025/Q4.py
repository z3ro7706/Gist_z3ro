import sys
input = sys.stdin.readline



def SpiceMerchant(cap, arr, idx, total):
    if(cap == 0 or idx >= len(arr)):
        return total
    w, v, r = arr[idx]
    if(cap >= w):
        return SpiceMerchant(cap-w, arr, idx+1, total+v)
    else:
        f = cap/w
        return int(total+v*f)
    
def combine(a, b):
    arr = []
    i = 0
    j = 0
    while True:
        if(i >= len(a)):
            while(j < len(b)):
                arr.append(b[j])
                j += 1
            break

        if(j >= len(b)):
            while(i < len(a)):
                arr.append(a[i])
                i += 1
            break

        if(a[i][2] >= b[j][2]):
            arr.append(a[i])
            i += 1
        else:
            arr.append(b[j])
            j += 1

    return arr


def merge_sort(a):
    if(len(a) <= 1):
        return a
    mid = len(a) // 2
    return combine(merge_sort(a[:mid]), merge_sort(a[mid:]))


x = list(map(int, input().split(',')))

if(len(x) < 1):
    exit(0)

cap = x[0]
new_x = x[1:]

if(len(new_x) % 2 != 0):
    exit(0)

spices = []
for i in range(0, len(new_x), 2):
    w = new_x[i]
    v = new_x[i + 1]
    r = v / w
    spices.append([w,v,r])

spices = merge_sort(spices)
print(int(SpiceMerchant(cap, spices, 0, 0.0)))
