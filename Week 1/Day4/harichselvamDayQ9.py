def countX(lst, x):
    count = 0
    for num in listt:
        if (num == x):
            count = count + 1
    return count
 
listt = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(f'{x} has occurred {countX(listt,x)} times')