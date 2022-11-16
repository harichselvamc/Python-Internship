dictionary=dict()
num=int(input("enter how many number of cities: "))
for i in range(num):
    city =input("enter the city name: ")
    temp=int(input("enter the temperature in celcious of the city: "))
    dictionary[city]=temp
print("created dictionary is : ",dictionary)

cityname=input("enter name of the city to check temperature of it : ")
print("temperature of the city is ",dictionary[cityname])