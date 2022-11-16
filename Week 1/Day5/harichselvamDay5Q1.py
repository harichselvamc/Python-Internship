year={'jan':1,'feb':2,'march':3,'april':4}                                     
listt=list(year.items())   #convet the given dict. into list
#In Python Dictionary, items() method is used to return the list
#with all dictionary keys with values.
listt.sort()#sort the list
print('Ascending order is',listt) #this print the sorted list 
listt=list(year.items())
listt.sort(reverse=True) #sort in reverse order
print('Descending order is',listt)
dict=dict(listt) # convert the list in dictionary 
print("Dictionary",dict) #the desired output is this sorted dictionary