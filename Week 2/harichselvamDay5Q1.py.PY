def binary_str_add(a,b):
    int_a = int(a,2) 
    int_b = int(b,2) 
    total = int_a + int_b
    return str(bin(total))[2:]  

a = input('Enter Binary a: ') 
b = input('Enter Binary b: ') 
res = binary_str_add(a,b) 

print(res) 