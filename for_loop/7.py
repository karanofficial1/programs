# Write a Python program that takes a string and builds a dictionary where keys are unique characters and
# values are the number of times each character appears

string = "karan"
c={}
for i in string:
    if i in c:
        c[i] +=1
    else:
        c[i] = 1

print(c)

    
    



    