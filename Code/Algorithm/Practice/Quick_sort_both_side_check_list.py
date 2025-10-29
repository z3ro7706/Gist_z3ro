def partition(A, l, h):
    pivot = A[l]
    i = l
    j = h

    while i < j:
        while i < h and A[i] <= pivot:
            i += 1
        while j > l and A[j] > pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
            print(A)

    A[l], A[j] = A[j], A[l]
    print(A)
    return j


def quick_sort(A, l, h):
    if l < h:
        print(A)
        pivot_index = partition(A, l, h)
        quick_sort(A, l, pivot_index - 1)
        quick_sort(A, pivot_index + 1, h)


arr=list(map(int,input().split()))
quick_sort(arr, 0, len(arr) - 1)
print(arr)

