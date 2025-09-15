def bin_search(start:int, end: int, lst:list,target_value:int): #binary search의 기본조건은 sort, 즉 정렬이 되어 있어야한다.
    if start > end: #만약 정렬이 되어 있지 않다면 return 0
        return 0
    else:
        mid = (start+end)//2 #중앙값을 가져옴. 이때 홀수개라면 앞쪽으로 배정됨
        mid_value = lst[mid] #중앙값을 list의 mid번째로 지정하자
        if mid_value == target_value: #같으면 찾았으므로 출력
            return 1
        elif mid_value > target_value: #만약 내가 찾으려는 숫자가 mid값보다 작다 = mid보다 왼쪽에 존재함
            return bin_search(start,mid-1,lst,target_value) #시작부터 미드값 전까지로 리스트를 다시 탐색함
        elif mid_value < target_value: #만약 내가 찾으려는 숫자가 mid값보다 크다 = mid보다 오른쪽에 존재함
            return bin_search(mid+1,end,lst,target_value) #미드값 뒤부터 끝가지로 다시 탐색함


N = int(input())
num_lst = list(map(int,input().split()))
M = int(input())
target_num_lst = list(map(int,input().split()))

num_lst.sort() #binaray search 이진탐색을 하기 위해서 오름차순으로 정렬을 해준다. 

for num in target_num_lst:
    print(bin_search(0,N-1,num_lst,num)) #위에 코드를 실행

#O(n) =nlogn