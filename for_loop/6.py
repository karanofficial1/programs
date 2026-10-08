# Write a Python program that loops through the sample string and counts the number of uppercase and
# lowercase letters separately. Spaces and punctuation must be ignored

string = input("Enter a string: ")
upper = 0
lower = 0
for i in string:
    if i.islower() == True:
        lower +=1
    elif i.isupper() == True:
        upper +=1
    else:
        pass
print("No. of uPPer case letter: ", upper)
print("no. of lower case letter: ", lower)