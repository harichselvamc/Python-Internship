numbers=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        numbers.append(str(x))
        
print("The Divisible Numbers are")
print (','.join(numbers))