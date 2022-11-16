nums = eval(input("Enter Number List : ")) 

def isMonotonic(nums):
    for i in range(len(nums)-1):
        if(nums[i]<=nums[i+1]):
            continue 
        else:
            return False  

    return True 

if(isMonotonic(nums) or isMonotonic(nums[::-1])):
    print(True) 
else:
    print(False)  