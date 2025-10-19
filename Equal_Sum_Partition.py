"""
Equal sum partition problem
정수만이 포함된 비어있지 않은 배열이 주어진다. 
주어진 배열을 두개의 subset 으로 나누었을 때 두 배열의 합이 같아지는 경우가 있는지 찾는다.

Input: nums = [1,5,11,5]
Output: true

Input: nums = [1,2,3,5]
Output: false
"""

import sys
input=sys.stdin.readline

def Equal_sum_partition(arr:list, i:int, target:int,dp):
    if(target==-1 and (i+1)==len(arr)):
        target=add_list(arr)
        dp = [[-1] * (target + 1) for j in range(len(x))]
        if((target)%2)!=0:
            return False
        
    if(target==0):
        return True
    if(i<0):
        return False
    if(target<0):
        return False
    if(dp[i][target]!=-1):
        return dp[i][target]
    else:
        dp[i][target]=Equal_sum_partition(arr,i-1,target-arr[i],dp) or Equal_sum_partition(arr,i-1,target,dp)
        return dp[i][target]

def add_list(arr:list):
    total=0
    for i in arr:
        total+=i
    
    return total

x=list(map(int,input().split()))
dp=[]
print(Equal_sum_partition(x,len(x)-1,-1,dp))
