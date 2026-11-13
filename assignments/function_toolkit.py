'''
Build a small library of reusable functions.
REQUIREMENTS
• Create area_rectangle(l, b) and area_circle(r) that return their results (use 22/7 for pi).
• Create average(*numbers) that accepts any number of values using *args.
• Create student_profile(name, age, school="Softyatri", **extra) that prints all details, including extra
keyword arguments.
• Write lambda functions for cube, is_even and percentage (marks obtained and total marks).
• Create a function that uses a global variable to count how many times it has been called.

'''
# • Create area_rectangle(l, b) and area_circle(r) that return their results (use 22/7 for pi).

PI = (22/7)
def area_rectangle(l,b):
    print("Area of rectangle: ", l * b)

def area_circle(r):
    return PI * r * r

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area_rectangle(length, breadth)
print("area of circle: ", area_circle(5))



# • Create average(*numbers) that accepts any number of values using *args.
def average(*args):
    return sum(args)/len(args)

avg = average(5,10,15,20,25)
print("Average is ", avg)



# Create student_profile(name, age, school="Softyatri", **extra) that prints all details, including extra
# keyword arguments.

def student_profile(name, age, school = "Softyatri", **kwargs):
    print("Name of student is :", name)
    print("Age of student is :", age)
    print("School is : ", school)
    for i,j in kwargs.items():
        print(i, ":", j)

student_profile("Karan", 28, "Soft Yatri", address ="Kanchanpur", contact = "986400")


# • Write lambda functions for cube, is_even and percentage (marks obtained and total marks).
cube = lambda x: x**3
num = int(input("Enter a number: "))
print(f"Cube of {num} is ", cube(num))

is_even = lambda x: x % 2 ==0
num = int(input("Enter a number: "))
if is_even(num):
    print("Even number")
else:
    print("Odd Number")


percentage  = lambda marks_obtained, total_marks: marks_obtained / total_marks * 100
marks = int(input("Enter your marks obtained: "))
total = int(input("Enter your total marks: "))

print("Percentage :", percentage(marks, total))


# • Create a function that uses a global variable to count how many times it has been called.
count = 0
def global_count():
    global count
    count += 1

global_count()
global_count()
global_count()
global_count()
global_count()

print("The function is called: ", count, "times")