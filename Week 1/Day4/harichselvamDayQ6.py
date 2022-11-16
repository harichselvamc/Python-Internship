import copy
number=[1,2,3,8,5,4]
print(number)
print(id(number))
number1=number
print(number1)
print(id(number1))
number[1]=10
print(number)
print(number1)#copy have a probelm the value on list have same memory location while we change value on a list that also reflect on another list
import copy
num2=copy.copy(number)
print(num2)
print(id(num2[2]))
print(id(number[2]))
a=[11,23,33,87]
b=copy.deepcopy(a)
print(a)
print(b)
print("this is a",id(a[2]))
print("this is b",id(b[2]))

print("1 index before",a[1])
a[1]=10
print("1 index after",a[1])
print(b)
print("this is a after change",id(a[1]))
print("this is b after change",id(b[1]))

