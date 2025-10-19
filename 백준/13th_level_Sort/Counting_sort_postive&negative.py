def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    count_arr = [0] * range_val

    # 카운팅
    for num in arr:
        count_arr[num - min_val] += 1

    # 누적합
    for i in range(1, range_val):
        count_arr[i] += count_arr[i - 1]

    output_arr = [0] * len(arr)

    i = len(arr) - 1
    while i >= 0:
        index = arr[i] - min_val
        output_arr[count_arr[index] - 1] = arr[i]
        count_arr[index] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output_arr[i]
