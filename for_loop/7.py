# Write a Python program that takes a string and builds a dictionary where keys are unique characters and
# values are the number of times each character appears

string = input("Enter a string: ")
c={}
for i in string:
    c[i] += 1
    print(c[i])

    
    



    