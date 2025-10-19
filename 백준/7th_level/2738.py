a, b = map(int, input().split())  # a*b matrix

arr = [[0] * b for _ in range(a)]
arr1 = [[0] * b for _ in range(a)]
arr2 = [[0] * b for _ in range(a)]

for i in range(a):  # 행 기준 입력
    insert=[]
    insert = list(map(int, input().split()))  # 한 줄씩 입력
    for j in range(b):
        arr1[i][j] = insert[j]

for i in range(a):  # 행 기준 입력
    insert=[]
    insert = list(map(int, input().split()))  # 한 줄씩 입력
    for j in range(b):
        arr2[i][j] = insert[j]

for i in range(a):  # 행 기준 덧셈
    for j in range(b):
        arr[i][j] = arr1[i][j] + arr2[i][j]

for row in arr:
    print(' '.join(map(str, row)))#join은 문자열만 입력이 가능하므로, int를 str로 변경 
