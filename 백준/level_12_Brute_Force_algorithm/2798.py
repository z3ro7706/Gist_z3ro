def Black_case(a: int, l: list, b=int):
    arr = []
    for i in range(0, a):
        for j in range(i + 1, a):
            for k in range(j + 1, a):
                val = l[i] + l[j] + l[k]
                if(val<=b):
                    arr.append(val)
        
    return max(arr)

x,y=map(int,input().split())
z = list(map(int, input().split()))

print(Black_case(x,z,y))