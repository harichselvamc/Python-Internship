# def soluindex(self,nums:list[int],target:int)->list[int]:
#     d={2,4,54,12,45}
#     for i in range(0,len(nums)):
#         value=nums[i]
#         difference=target-value
#         if value not in d:
#             d[difference]=i
#         else:
#             currentindex=i
#             previousindex=d[value]
#             return[currentindex,previousindex]
    

# target=input("enter the number")
# print(soluindex)

# def findindex(a,b):
#     if a in b:
#         return b.index(a)
#     else:
#         b.append(a)
#         b.sort()
#         return(b.index(a))

# b1=input("Enter the number: ")
# b=b1.split(",")
# a=input("Enter A TARGET number: ")
# print(findindex(a,b))
        
# number=input("Enter the Number: ")
# number1=number.split(",")
# numbers=number1
# numbers.sort()
# result = [item * numbers for item in numbers]
# print(numbers)

my_list = [2, 4, 6]

# result = [item * my_list]
# for item in my_list:
#     result=my_list*my_list
    
#     print(result)
result=my_list*my_list
print(result)  