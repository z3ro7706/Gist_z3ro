def binary_search(arr,k):
    length=len(arr)
    arr_new=[]
    p=length//2
    if(len(arr)<=1):
        if(len(arr)==1):
            if(arr[0]==k):
                return True
            else:
                return False
        else:
            return False
    if(arr[p]>k): #찾고자 하는 값이 왼쪽에 있음
        arr_new=arr[:p]
    elif(arr[p]<k): #찾고자 하는 값이 오른쪽에 있음
        arr_new=arr[p+1:]
    elif(arr[p]==k): #원하는 값 찾음
        return True
    else:
        print("Have some problem")
    return binary_search(arr_new,k)