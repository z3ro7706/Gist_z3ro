import random #앞에서부터,자신을 포함한 최소값을 찾고, 최소값과 앞의값의 위치를 바꿔줌. O(n)=n^2
#https://youtube.com/shorts/HRwi5gwlB0U?si=OkrjU8NQExmneSAZ

def find_min_index(A):
  min_idx = 0
  for i in range(1, len(A)): #남은 갯수만큼 진행
    if A[i] < A[min_idx]: #만약 더 작은 값이 나온다면
      min_idx = i #min_idx를 더 작은 번호로 바꾸기. 
  return min_idx #가장 작은 값의 번호 리턴

def selection_sort(A):
  if len(A) == 0: #만약 1개라면 그대로 리턴
    return A

  k = find_min_index(A) #가장 작은 값의 번호를 받음
  return [A[k]]+selection_sort(A[:k]+A[k+1:]) #가장 작은 번호를 앞으로 가져오고, 나머지 부분에 대해서 생각함(새로운 list 생성)

# w = [random.randrange(1000) for i in range(100) ]
# print(w)
# ws = selection_sort(w)
# print(ws)