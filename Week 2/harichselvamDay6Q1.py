st = input("Enter Stirng : ")
state = False  
for i in range(1,len(st)//2):
    sub_string = st[:i] 
    rep = sub_string*(len(st)//len(sub_string)) 
    if(rep == st):
        state = True 
        break 

print(state)  

