arr=list(map(int,input("Enter the numbers in Sorted Order : ").split(",")))
target=int(input("enter the number"))


def target_pair(arr,target):
    for i in range(len(arr)):  
        if(arr[i]>target): 
            break
        rem = target - arr[i]
        ind = -1  
        try:
            ind = arr.index(rem) 
            break
        except Exception as e:
            pass 

    if(ind>0):
        return [i+1,ind+1]   
    else:
        return 0

print(target_pair(arr,target)) 
 


