x = int(input())  # 받을 word list 개수

arr = [[0]*3 for _ in range(x)]  # 각 줄이 독립된 리스트를 갖도록 생성

for i in range(x):
    a = input()
    arr[i][0] = len(a)       # 단어 길이
    arr[i][1] = a            # 단어 자체 (사전 정렬용)
    arr[i][2] = a            # 원본 단어

def len_sort(arr):
    arr_new = []  # 최종 결과 리스트

    for i in range(0, 51):
        arr_append = []
        arr_append_same = []

        for k in range(x):
            if arr[k][0] == i:  # 해당 길이인 단어만
                is_duplicate = False
                for item in arr_append:
                    if arr[k][2] == item[2]:  # 단어 기준 중복 제거
                        is_duplicate = True
                        break
                if not is_duplicate:
                    arr_append.append(arr[k])

        if len(arr_append) >= 1:
            # 단어 전체 기준으로 정렬 (사전순 정렬)
            arr_append.sort(key=lambda item: item[2])
            arr_append_same.extend(arr_append)

        arr_new.extend(arr_append_same)

    return arr_new

arr_sort = len_sort(arr)

for i in range(len(arr_sort)):
    print(arr_sort[i][2])  # 단어만 출력
