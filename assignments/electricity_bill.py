'''
Write a program that calculates a household electricity bill using slab rates.
REQUIREMENTS
• Accept the number of units consumed.
• Apply the rates: first 20 units at Rs. 5, next 30 units at Rs. 8, and all remaining units at Rs. 12.
• Add a fixed service charge of Rs. 50 to every bill.
• Use the ternary operator to print "High usage warning" when the total bill exceeds Rs. 1000.
'''


unit = int(input("Enter your Units consumed: "))
service_charge = 50
if unit <=20:
    amount = unit * 5

elif unit<=50:
    amount = (20 * 5) + (unit-20)*8

else :
    amount = (20 * 5) + (30 * 8) + (unit-50)*12


print("Bill Amount: Rs.", amount)
bill= amount+ service_charge
print("Bill Amount with service charge =Rs.",bill )

print("You are using alot of electricity.") if bill > 1000 else None




