# Write a Python program that asks the user to enter a number and prints its complete multiplication table from 1 to 10

num = int(input("Enter a number: "))

for i in range(1,11):
    print(num, "*", i , "=", num * i)