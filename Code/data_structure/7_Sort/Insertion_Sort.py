import random #insert sort의 경우 1줄로 탐색하면서, 작은 값을 앞의 위치를 찾아서 넣어주는 방식일 이야기한다. 
#https://youtube.com/shorts/ZZ-Oz1IFfPg?si=9mRsfvM8oO1xoTx4
def insert_sort(A): #만약 A의 길이가 0 이라면, 리스트가 1개 존재하는 것이다. 
  if len(A) == 0:
    return A #1개의 원소만 return 해주면 됨

  for i in range(1, len(A)): #앞에 있는 원소에 대해서 계속해서 반복하므로 결국 자신의 자리를 찾아가게 된다. 
    for j in range(0, i):
      if A[i] < A[j]: #만약 뒤의 원소의 크기가 더 클 경우
        A[i], A[j] = A[j], A[i] #둘의 위치를 바꾼다. 

  return A

w = [ random.randrange(1000) for i in range(100) ]
print(w)
ws = insert_sort(w)
print(ws)

#O(n)=n(n-1)/2=n^2