list = []
number = int(input('How many numbers : '))
for n in range(number):
    numbers = int(input('Enter number : '))
    list.append(numbers)
print("Largest element in the list is :", max(list), "\nSmallest element in the list is :", min(list))