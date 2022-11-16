star = 5
for i in range(0,star):
  for j in range(0,i+1):
    print("*",end = " ")
  print()
for i in range(star+1,0,-1):
  for j in range(1,i-1):
    print("*",end = " ")
  print()



