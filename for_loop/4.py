''' Write a Python program that accepts a string from the user and counts the total number of vowels (a, e, i, o,u)
     it contains, ignoring case 
    '''
count = 0
string = input("Enter a string: ").lower()
for i in string:
    if i in "aeiou":
        count +=1

print("Total number of vowels:", count)