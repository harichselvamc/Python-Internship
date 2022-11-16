digits = eval(input("Enter the large Integer: ")) 
st = ''.join(str(i) for i in digits) 
num = int(st)+1 
res = list(map(int,[i for i in str(num)]))
print(res) 
