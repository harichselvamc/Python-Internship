arr = list(map(int,input('Enter array of numbers: ').split(",")))  
k = int(input("Enter a step value to rotate: ")) 

for i in range(k):
    arr.insert(0,arr.pop()) 

print(arr) 