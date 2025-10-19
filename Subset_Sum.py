"""

부분집합 합 문제(Subset sum Problem) 
문제 : 음수가 아닌 정수로 이루어진 집합 S와 임의의 정수 X가 주어질 때, 
S의 부분집합 중에서 그 원소의 합이 X와 같은 부분집합이 존재하는가?
S = {13, 79, 45, 29}
x = 42 -> True (13 + 29)
x = 25 -> False
test case : 13 79 45 29

"""
import sys
input=sys.stdin.readline

def subset_sum(arr:list, i:int, target:int,dp,use:list):
   
    if(target==0):
        return 1
    if(i<0):
        return 0
    if(target<0):
        return 0
    
    if(dp[i][target]!=-1):
        return dp[i][target]
    else:
        if((subset_sum(arr,i-1,target-arr[i],dp)==0 and  subset_sum(arr,i-1,target,dp)==0)):
            dp[i][target] = 0
        else:
            use.append(arr[i])
            dp[i][target] = 1
        
        return dp[i][target]


x=list(map(int,input().split()))
t=int(input())
use=[]
dp_initial = [[-1] * (t + 1) for i in range(len(x))]
print(subset_sum(x,len(x)-1,t,dp_initial,use))

