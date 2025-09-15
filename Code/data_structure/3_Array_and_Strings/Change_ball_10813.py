N, M = map(int, input().split()) #받은 값을 list형식으로 정리 -> [N,M]

baskets = list(range(1, N + 1)) #basket을 1~ n까지를 리스트로 받아냄 (1,n+1)임에 주의하자

for _ in range(M):
    i, j = map(int, input().split()) 
    baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1] #받은 값의 위치를 변경함

print(" ".join(map(str, baskets))) #출력

#O(n) = n