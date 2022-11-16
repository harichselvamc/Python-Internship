colors = ['red','blue','green','yellow','black']
#finding length
print(len(colors))
#slicing the list
print(colors[0:3])
#negative slicing
print('Last element in the list is: ',  colors[-1])
#adding element
for i in range(2, 6):
    colors.append(i) 
print(colors)
#extending element
colors.extend("hello")
print("List after extending the String is:", colors)
#deleting element

