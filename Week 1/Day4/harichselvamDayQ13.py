item=["hello","this","that"]
print(item)
alist = []#empty list
alist.append(item)# append new item into list at the end of the list
print(alist)
item.insert (3,"chennai")#(index,item)append new item into list at a specific index
print(item)
item.pop(0)# remove an item from the list based on index
print(item)
item.remove("this")# remove an item from the list based on item value
print(item)
item.sort()# sort the items in ascending order, note that the data types must be similar
print(item)
item.reverse()# reverse the order of the items
print(item)
aset = set()#an empty set
aset = {'one', 2}#a set
print(aset)
aset.add('c')# adding item to a set
print(aset)
aset.remove('one')# removing an item from a set, raise keyError if item does not exist
print(aset)
aset.discard('one')# removing an item from a set, no keyError if item does not exist
print(aset)
aset.pop()# remove the first item from a set and return it
print(aset)
aset.clear()# remove all items from a set
print(aset)
adict = {}# define an empty dictionary
adict = {"one":1, "two":2}# define a dictionary
print(adict)
adict[1] = "hello" # adding new items to the dictionary
print(adict)
adict[2] = "python" # adding another items to the dictionary
print(adict)
adict.keys()# display the keys in the dictionary
print(adict)
adict.values()# display the values in the dictionary
print(adict)
adict.items()# display the items in the dictionary
print(adict)
mytuple = ("thuraiyur", "tennur", "trichy")
#tuples are ordered, it means that the items have a defined order, and that order will not change, unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.Allow Duplicates
print(mytuple)
print(len(mytuple))
print(type(mytuple))
thistuple = tuple(("annanagar", "koyembedu", "omr"))
print(thistuple)
print(len(thistuple))
print(type(thistuple))


