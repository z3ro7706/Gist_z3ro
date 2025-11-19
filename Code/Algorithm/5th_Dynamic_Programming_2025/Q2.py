import sys
input=sys.stdin.readline

def PlateBreaking(n,dp):
    for i in range(1,n+1):
        dp[i]=dp[i-1]+i
        
        if(dp[i]>=n):
            return dp[i]
		    
	
n,m=map(int,input().split(','))
dp=[0 for _ in range(n+1)]
print(PlateBreaking(n,dp))