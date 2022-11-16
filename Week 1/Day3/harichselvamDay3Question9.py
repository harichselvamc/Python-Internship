color1 = [1, 3, 4, 6, 8]
color2 = [4, 5, 6, 2, 10]

print ("Original list 1 : " + str(color1))
print ("Original list 2 : " + str(color2))

final = []
for i in range(0, len(color1)):
	final.append(color1[i] + color2[i])

print ("Resultant list is : " + str(final))