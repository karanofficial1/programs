''''
Create a program with two parts that demonstrate loop control.
REQUIREMENTS
• Part A: Accept a size n and print a right-angled star triangle with n rows, followed by a number pyramid
with n rows.
• Part B: Print the numbers from 1 to 50. Print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and
"FizzBuzz" for multiples of both.
• Use nested loops for Part A and the modulus operator for Part B.
'''

# for A
num = int(input("Enter a size of triange.: "))
for i in range(num+1):
    print(i * '*')


# for B

for i in range(1,51):
    if i% 3 ==0  and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 ==  0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")

    else:
        print(i) 
    
