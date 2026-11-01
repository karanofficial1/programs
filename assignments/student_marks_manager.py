'''
Create a program that records and analyses the marks of five students.
REQUIREMENTS
• Accept the name and marks of 5 students and store them in a dictionary.
• Assign a grade to each student: A (80 and above), B (60 to 79), C (45 to 59), Fail (below 45).
• Display the class average and the name of the topper.
• Display a ranking list from the highest marks to the lowest marks.
'''

student = {'pratik': 85, 'prince': 25, 'karan': 40, 'djfkdj': 65, 'dkjfkdj': 80}
# student = {}
# for i in range(5):
#     name = input("Enter your name: ")
#     marks = int(input("Enter your marks: "))
#     student[name] = marks

# average = sum(student.values())  # find sum
# print(average)

for i, j in student.items():
    if j >= 80 :
        grade = "A"
    elif j > 60 and j < 80 :
        grade = "B"
    elif j >= 45 and j <= 59 :
        grade = "C"
    else:
        grade = "Fail"
    student[i] = {'marks': j, 'grade': grade }
    
print(student)

total = 0
toper = ""
highest = 0
for i, j in student.items():
    total = total + j['marks']
    if j['marks'] > highest:
        highest = j['marks']
        toper = [i]
    elif j['marks'] == highest:
        toper.append(i)

print("Toper = ", toper)
average = total/len(student)
print("Avereage of marks: ",average)


# Rank