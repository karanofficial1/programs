# Write a Python program that generates and prints the first 10 terms of the Fibonacci series using a loop.
a = 0
b = 0
for i in range(0,11):
    a, b = b, a+b
    print(b)

