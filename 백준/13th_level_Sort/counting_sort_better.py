def counting_sort(arr):
    # 최대값 찾기
    max_val = max(arr)
    # 카운트 배열 초기화
    count_arr = [0] * (max_val + 1)

    # 입력 배열의 요소 세기
    for num in arr:
        count_arr[num] += 1

    # 누적 카운트 배열 계산
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    # 결과 배열 초기화
    output_arr = [0] * len(arr)

    # 결과 배열 만들기
    i = len(arr) - 1
    while i >= 0:
        output_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
        i -= 1

    # 결과 복사
    for i in range(len(arr)):
        arr[i] = output_arr[i]

# 예시
arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print(arr)
