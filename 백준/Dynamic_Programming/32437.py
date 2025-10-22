import sys
input=sys.stdin.readline

def Fraction(arr,n):
    if(n==0):
        return 1
    if(n==1):
        return 2
    
    if(arr[n-1][0]!=0 and arr[n-2][0]!=0):
        return arr[n-1][0]+arr[n-2][0]
    else:
        arr[n][0]=Fraction(arr,n-1)+Fraction(arr,n-2)
        arr[n][1]=arr[n-1][0]+arr[n][0]
        return arr[n][0]

    

x=int(input().strip())
arr=[[0]*2 for _ in range(0,x+1)]
print(Fraction(arr,x-1))
