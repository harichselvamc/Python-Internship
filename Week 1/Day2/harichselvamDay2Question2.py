#this is one type
numbers= range(10,21)

for number in numbers:
    i = number*number
    if i % 2 ==0:
        continue
    else:
        print(f"{i} is an odd number")
        
        
#this is second type     
numbers=range(10,21)

for number in numbers:
    if number % 2 ==0:
        continue
    else:
        
        print(f"{number} is an odd number")
        print(number*number,"is the square of the odd number")


