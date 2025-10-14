x = int(input())
arr = list(map(int, input().split()))
arr_other = []
value = 1 

while True:
    if len(arr) == 0 and len(arr_other) == 0:
        print("Nice")
        exit(0)
    
    if arr_other and arr_other[-1] == value:
        arr_other.pop()
        value += 1
    elif arr and arr[0] == value:
        arr.pop(0)
        value += 1
    elif arr:
        arr_other.append(arr.pop(0))
    else:
        print("Sad")
        exit(0)
