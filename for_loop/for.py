names = ['karan', 'sujan', 'ramesh', 'suman', 'shyam']
op=[]
for i in names:
    if i.startswith("s"):
        print(i)
        op.append(i)

print(op)


age_group =[17,18,13,88,34,40,45,20,91,25]

op= []
for i in age_group:
    if i>=18:
        op.append(i)
print(op)



nums = [12,13,11,3,5,2,4]
even=[]
for i in nums:
    if i%2==0:
        even.append(i)
print(even)


# Write a program to calculate the sum of numbers from 1 to 100.
sum = 0
for i in range(1,101):
    sum +=i
print(sum)

# Write a program to print each character of: word = "Python"

word = "Python"
for i in word:
    print(i, end=" ")

# Write a program to count the number of characters in a string using a for loop.
word = input("\nEnter word: ")
num = 0
for i in word:
    num +=1
print("\nnumber of characters: ", num)
    


