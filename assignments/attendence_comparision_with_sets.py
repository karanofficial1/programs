'''
Two lists store the names of students present on Monday and Tuesday. Both lists may contain duplicate
names.
REQUIREMENTS
• Convert both lists into sets to remove duplicates.
• Display the students present on both days.
• Display the students present only on Monday and only on Tuesday.
• Display the students present on at least one day.
• Given a full class list, display the students absent on both days
'''
full_class = ["Karan", "Pratik", "Prince", "Gopal", "Lalit","Golden", "Blade","Sita","Gita", "Ram", "Hari","Shyam"]
monday = ["Karan", "Pratik", "Prince", "Gopal", "Lalit"]
tuesday = ["Karan", "Pratik", "Prince", ]

full_class_set = set(full_class)
mon_set = set(monday)
tues_set =set(tuesday)
remove_duplicates = mon_set.union(tues_set)
print("Student names after removing duplicates are: ",remove_duplicates)

print("Student present on both days: ", mon_set.intersection(tues_set))
only_monday = mon_set.difference(tues_set)
only_tuesday = tues_set.difference(mon_set)
only_monday_tuesday = only_monday.union(only_tuesday)
print("Student present only on monday and only on tuesday are: ", only_monday_tuesday)
print("Student names Present at least on one day: ",remove_duplicates)

print("Student absent on both days: ",full_class_set.symmetric_difference(remove_duplicates))
