score = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"] 
count = 0
for i in score:
  if i == "Pass":
    count += 1
print(f'You passed {count} times') 