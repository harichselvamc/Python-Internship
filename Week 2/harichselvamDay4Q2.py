lst = eval(input("Enter The array Form : ")) 
st = '' 
for i in lst:
    st += str(i) 

number = int(st) 
k = int(input("Enter the value of k: ")) 
st = str(int(st) + k)  
st = str(st) 
lst = list(map(int,list(st))) 
print(lst)  
 