Colors = ["Yellow","Green","White","Black"]
Fruits = ["Apple","Papaya","Mango","Orange"]
Animals = ["Tiger","Lion","Deer","Zebra"]
cities=["Chennai","Bangalore","Delhi","Pune"]


inputfirst = input("Enter a name :")
input1 =inputfirst.capitalize()

inputsecond = input("Enter a name :")
input2 =inputsecond.capitalize()

if input1 in Colors and input2 in Colors:
    print("Both are Colors")

elif input1 in Fruits and input2 in Fruits:
    print("Both are Fruits")

elif input1 in Animals and input2 in Animals:
    print("Both are Animals")


elif input1 in cities and input2 in cities:
    print("Both are in same Country")

else:
    print("They don't belong to same category")