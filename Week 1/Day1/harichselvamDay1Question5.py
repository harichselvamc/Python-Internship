for i in range(1,51):
    
  if i%10 == 0:
    tired = input("Are you tired?")
    if tired == "YES":
      print("You didn't finish the race")
      break

if i==50:
  print("Congratulations!! You finished the race")
else:
  print(f"congrats! You still ran {i} KM")