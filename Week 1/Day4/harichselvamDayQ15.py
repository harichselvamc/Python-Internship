num=[1,2,33,42,32,12,543,54]

#filter works upon whether the value is true it wont accept if it return false.
def filters(data):
    if data %2==0:
        return True
    else:
        return False
    
output=filter(filters,num)
print(list(output))