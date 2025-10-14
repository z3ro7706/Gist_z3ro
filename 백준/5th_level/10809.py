
key = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

arr=list(input())
ans=[]
for i in range(len(key)):
    ans.append(-1)

val=0
for i in range(len(key)):
    for j in range(len(arr)):
        if(key[i]==arr[j]):
            ans[i]=j
            break

print(*ans)