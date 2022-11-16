def word_length(s):
    word_list = s.split() 
    n = len(word_list[-1]) 
    return n 

s = input("Enter a String : ") 
n = word_length(s) 

print('Length of Last Word :',n) 