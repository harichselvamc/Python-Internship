arr = list(map(int,input("Enter The array: ").split(",")))   

def squared_array(arr):
    squared = [i*i for i in arr]
    squared.sort() 
    return squared  

print(squared_array(arr))   