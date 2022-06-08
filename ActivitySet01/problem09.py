# Lists

file_name = raw_input("Enter file name: ")
open_file = open(file_name)
l = list()                      
for line in open_file:   
    word= l.rstrip().split()   
    for i in word:           
        if i in l:         
            continue               
        else :                     
            l.append(i)       
l.sort()                         
print (l)       