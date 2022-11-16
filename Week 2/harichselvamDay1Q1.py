# def findindex():
#     limit=("Enter the limit of number: ")
    
#     a=input("Enter the numbers:")
#     a1=a.split(",")
#     b=int(input("Enter the Target value: "))
    
#     if b in a1:
#         print("Yes,its presented")
        
#     else:
#         print("not found")
#     print(a1)    
# findindex()

def findindex(a,b):
    if a in b:
        return b.index(a)
    else:
        b.append(a)
        b.sort()
        return(b.index(a))

b1=input("Enter the number: ")
b=b1.split(",")
a=input("Enter A TARGET number: ")
print(findindex(a,b))



# def solution():
#     l=0;
#     h=numbers*length
    