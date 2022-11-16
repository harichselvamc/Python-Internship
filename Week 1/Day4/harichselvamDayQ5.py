#reverse() method edits the list to be in a reversed order.
number=[1,2,3,8,5,4]
number.reverse()
print(number)
#reversed() method takes a list and returns an iterator of it in reverse order.
num=reversed(number)
num=list(num)
print(num)