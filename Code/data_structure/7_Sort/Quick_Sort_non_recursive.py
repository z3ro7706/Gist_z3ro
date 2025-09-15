import random 
#Quick short의 경우, pivot과 비교하였을때, 작으면 i를 한칸 키우고, 그 값을 맨앞으로 가져온다. 만약 크다면 j를 1 키운다.
#Quickshort 의 경우 완벽하게 정렬되지 않음에 주의하자 
#https://youtube.com/shorts/-5cEMbsyMgs?si=tbObvOrc89l5v7PF
# partition range a[lo:hi+1] and return index of pivot
#best case O(n)=nlogn, worst case O(n)=n^2
def partition(a, lo, hi):
  p = (lo + hi)//2
  pivot = a[p]
  a[p] = a[hi]  # Swap pivot with last item
  a[hi] = pivot

  i = lo - 1
  j = hi
  while i < j:
    i += 1
    while a[i] < pivot:
      i += 1
    j -= 1
    while a[j] > pivot and j > lo:
      j -= 1
    if i < j:
      t = a[i]; a[i] = a[j]; a[j] = t  # swap a[i] and a[j]
  a[hi] = a[i]
  a[i] = pivot # Put pivot where it belongs
  return i     # index of pivot

# sort range a[lo:hi+1]
def quick_sort(a, lo, hi):
  if (lo < hi):
    pivot = partition(a, lo, hi)
    quick_sort(a, lo, pivot - 1)
    quick_sort(a, pivot  + 1, hi)


n = 10000
w = [random.randrange(1000000) for _ in range(n)]
print(w[:100])
quick_sort(w, 0, n - 1) # in-place
print(w[:100])