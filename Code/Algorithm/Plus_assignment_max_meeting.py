#If you have as many meetings as possible
import sys
input = sys.stdin.readline


end_list = list(map(int, input().split()))
time_list = list(map(int, input().split()))
n=len(end_list)
if(n!=len(time_list)):
    print("Error")
    exit(0)

    
arr = []



for i in range(n):
    end = end_list[i]
    time = time_list[i]
    start = end - time
    arr.append([start, end])


arr.sort(key=lambda x: (x[1], x[0]))
count = 0
end = 0


for i in range(n):
    if arr[i][0] >= end:
        end = arr[i][1]
        count += 1


print(count)
