import random #2칸씩 사이즈를 비교하여서, 정렬한다. 한사이클을 돌리면 가장 뒤에 가장 큰 값이 남게 되므로 이를 반복한다. O(n)=n^2
#https://youtube.com/shorts/y2AghjB4Wxs?si=-nzHKyrqLDy7O2Of
def bubble_sort(A):
  if len(A) == 0:
    return A

  for i in range(len(A)-1):
    if A[i] > A[i+1]:
      A[i], A[i+1] = A[i+1], A[i]

  return bubble_sort(A[:-1]) + [A[-1]]

w = [random.randrange(1000) for i in range(100) ]
print(w)
ws = bubble_sort(w)
print(ws)