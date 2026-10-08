''' Write a Python program that validates a user's password against the five rules below. Clearly indicate which
specific requirements were NOT met.
Requirements:
u At least 8 characters long
u Contains at least one uppercase letter (A-Z)
u Contains at least one lowercase letter (a-z)
u Contains at least one digit (0-9)
u Contains at least one special character (! @ # $ % ^ & * etc.
'''
# password = input("Enter a password: ")
# if (len(password) >= 8):
#     for i in password:
#         if i.islower(): 
#             if i.isupper():
#                 if i.isdigit():
#                     if i in "!@#$%^&*":
#                         print("Requirements met.")
#                     else:
#                         print("Must contain one special character")
#                         break
#                 else:
#                     print("Must contain a digit")
#                     break
#             else: 
#                 print("Must contain at least one uppercase letter")
#                 break
#         else:
#             print(" Must contain at least one lowercase letter") 
#             break     
# else:
#     print("your password is less than 8.")

password = input("Enter a password: ")

lower = False
upper = False
digit = False
special = False


for i in password:
    if i.isdigit():
        digit = True
    if i.isupper():
        upper = True
    if i in "!@#$%^&*":
        special = True
    if i.islower():
        lower = True


if digit and upper and special and lower:
    print("Password is VALID.") 
    print("All requirements are met.")
else:
    if len(password) < 8:
        print("[x] Must be at least 8 characters long")
    if digit == False:
        print("[x] Must contain at least one digit")
    if upper == False:
        print("[x] Must contain at least one uppercase letter")
    if special == False:
        print("[x] Must contain at least one special character")
    if lower == False:
        print("[x] Must contain at least one lowercase letter")


    

