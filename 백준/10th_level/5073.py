while True:
    a, b, c = map(int, input().split())
    
    # 종료 조건
    if a == 0 and b == 0 and c == 0:
        break
    
    # 가장 긴 변을 찾고 나머지 둘의 합과 비교
    sides = sorted([a, b, c])
    
    if sides[2] >= sides[0] + sides[1]:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
