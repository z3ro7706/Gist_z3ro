n = int(input()) #몇개를 받을것인가
map_array = [[0]*100 for _ in range(100)] #map을 100 * 100 좌표계를 만들기 [0,0,0,0, ...,0] 100기로 채워서 밑으로 100개 쌓기

for _ in range(n): #받는 for문 돌리기
    x, y = map(int, input().split()) #시작지점 잡기
    for i in range(y, y+10): #세로지점 10개
        idx_y = i
        for j in range(x, x+10): #가로지점 10개
            idx_x = j #지금의 위치잡기
            if map_array[idx_y][idx_x] == 0: #만약 비여있는 공간이라면
                map_array[idx_y][idx_x] = 1 #새로운 값 1로 채워주기
            else:
                pass #끝나면 돌리기
            
sum_array = 0
for i in range(100):
    sum_array += sum(map_array[i]) #모든 map의 합을 더하기
print(sum_array)

#O(n)=n