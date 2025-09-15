import random #작게 쪼개여서 정렬후, 쪼갠 조각들을 다시 정렬(2개의 배열을 비교하며 넣기) O(n)=nlogn
#https://youtu.be/bKT9yyRslm8?si=Gv-Jllwkxej9O6lp

def merge(a, b): #크기를 비교해서 넣는것 (Merget sort 특성상 제귀적으로 호출되어야 하기 때문에 따로 정의가 필요)
  i = 0
  j = 0
  res = []
  while i < len(a) and j < len(b):
    va = a[i]
    vb = b[j]
    if va <= vb: #작은걸 앞에, 큰걸 뒤에 저장
      res.append(va)
      i += 1
    else:
      res.append(vb)
      j += 1
  # now just copy remaining elements
  # (only one of these can be non-empty)
  res.extend(a[i:])
  res.extend(b[j:])
  return res

def merge_sort(a):
  if len(a) <= 1:
    return a
  mid = len(a) // 2 #중간값 지정
  left_half = merge_sort(a[:mid]) #중간값을 기준으로 짜르기
  right_half = merge_sort(a[mid:])
  return merge(left_half, right_half)

n = 10000
w = [random.randrange(1000000) for _ in range(n)]
print(w[:100])
w = merge_sort(w) 
print(w[:100])