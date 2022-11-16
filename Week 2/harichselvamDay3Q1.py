arr = list(map(int,input("Enter an array of sorted numbers: :").split(","))) #[-1,0,3,5,9,12]l
target = int(input("Enter a number to search: ")) 

def binary_search(arr,target,left,right):
    if(left > right):
        return -1
    mid = (left+right)//2
    if(arr[mid] == target):
        return mid
    elif(arr[mid]>target):
        return binary_search(arr,target,left,mid-1) 
    else:
        return binary_search(arr,target,mid+1,right)  
index = binary_search(arr,target,0,len(arr)-1) 
if(index>=0):
    print("Target found at index",index) 
else:
    print("Target not found in given array")  