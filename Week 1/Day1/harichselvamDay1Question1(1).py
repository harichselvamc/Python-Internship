Colors = ["Yellow", "Green", "White", "Black"]
Fruits = ["Apple", "Papaya", "Mango", "Orange"]
Animals = ["Tiger", "Lion", "Deer", "Zebra"]

user = input(
  "Enter color, fruit or animal name : ")  #getting input from the user
giveninput = user.capitalize(
)  #wheter the user may type in the input as small letter or capital letter ,i used capitalize function to change the input into First letter should turned to capital for the comparision

if giveninput in Colors:
  print(giveninput, "is a Color")

elif giveninput in Fruits:
  print(giveninput, "is a Fruit")

elif giveninput in Animals:
  print(giveninput, "is an Animal")

else:
  print("Sorry! not in any category")
