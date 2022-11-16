givendata = {"John":1400000, 'Smith':1300000, 'Alice':3200000, 'Daniel':3200000}
print("information on Employees and their Salary")
userinput = input('What Do You Want With This Data (Print\Add\Remove\Query) : '.title())
if userinput=='Print':
  for i in givendata.items():
    print(i[0],'==>',i[1])
elif userinput == 'Add':
  newname = input('Enter A Name Of New Employee : ')
  if newname in givendata.keys():
    print('This Name Is Already In Data')
  else:
    newsalary = int(input('Enter The Salary Of Employee : '))
    givendata[newname]=newsalary
    for j in givendata.items():
      print(j[0],'==>',j[1])
elif userinput == 'Remove':
  remove = input('Enter A Employee Name To Remove : ')
  if remove in givendata:
    del givendata[remove]
    for k in givendata.items():
      print(k[0],'==>',k[1])
  else:
    print('Employee Does Not Exist')
elif userinput == 'Query':
  quer = input('Enter The Name Of The Employee Wants To Query')
  if quer in givendata:
    print(givendata[quer])
  else:
    print('The Name Does Not Exist')
else:
  print('Enter Only Valid Input')