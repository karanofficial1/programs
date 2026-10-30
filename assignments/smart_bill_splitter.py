'''
Write a program that calculates how a restaurant bill is divided among a group.
REQUIREMENTS
• Accept the bill amount, tip percentage and number of people from the user.
• Convert the inputs to the correct data types.
• Calculate and display the tip amount, the total bill and each person's share.
• Format every monetary value to 2 decimal places using f-strings.
'''

amount = float(input("Enter your bill amount : "))
tip = int(input("Enter your tip percentage: "))
number_of_people = int(input("Enter number of people : "))

tip_percent = tip/100

tip_amount = amount * tip_percent
total_bill = tip_amount + amount
each_person_share = total_bill/number_of_people

print(f"Tip Amount: Rs.{tip_amount:.2f}")
print(f"Total Bill: Rs.{ total_bill:.2f}")
print(f"Per Person : Rs.{each_person_share:.2f}")


