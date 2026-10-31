'''
Develop a menu-driven contact management application.
REQUIREMENTS
• Store contacts in a nested dictionary, for example: {"Ram": {"phone": "9800000000", "email":
"ram@mail.com"}}.
• Provide options to add, search, update, delete and list all contacts.
• Prevent duplicate contact names.
• Validate email addresses: the email must contain "@" and a "." after it.
• Implement each feature as a separate function and keep the menu running until the user chooses Exit.
'''

contact = { 
            "Ram": {
        "phone": "980",
        "email": "ram@mail.com"
    },
    "Hari": {
        "phone": "981",
        "email": "hari@mail.com"
    }
            }


def add():
    print("Plz enter your Details.")
    name = input("Enter a name: ").title()
    global contact
    if name in contact:
        print("Name already Exists. Plz enter another name.")
        return add()
    else:
        phone = input("Enter your phone number:")
        email = input("Enter your email address: ")
        email_true = email_validate(email) 
        if email_true:
            contact[name.title()] = {
                        "phone": phone,
                        "email": email
                        }   
            print("Contact added Successfully.") 
            return option_fun()
        else:
            print("please enter valid email address")
        return add()

       

def search():
    name_phone = input("Enter name or phone number to Search: ")
    global contact
    for i,j in contact.items():
        if i == name_phone:
            print(f"Contact name: {name_phone}")
            for key,value in j.items():
                print(key ,":", value)
            return option_fun()
        else:     
            for key,value in j.items():
                if value== name_phone:
                    print("Contact Name: ", i)
                    print(f"Contact number: {name_phone}")
                    print(f"Email Address: {j["email"]}") 
                    return option_fun()   
            else:
                print("Contact Not found.")
    else:
        print("Contact Not found.")

def update():
    name_phone = input("Enter name or phone number to update: ")
    global contact   
    for i,j in contact.items():
        if i == name_phone or j["phone"] == name_phone:
            print("Contact found!")
            print("Name:", name_phone)
            print("Old Phone:", j["phone"])

            new_phone = input("Enter new phone number: ")

            contact[i]["phone"] = new_phone

            print("Phone number updated successfully!")
            return

    print("Contact not found!")
            
           


def delete():
    name_phone = input("Enter name or phone number to delete: ")
    global contact   
    for name, info in contact.items():
            if name == name_phone:
                contact.pop(name)
                print("Contact deleted successfully!")
                return option_fun()

            elif info["phone"] == name_phone:
                contact.pop(name)
                print("Contact deleted successfully!")
                return option_fun()

    print("Contact not found!")
    return option_fun()

def list_all_contact():
    global contact
    for i,j in contact.items():
        print("Name:", i )
        for key,value in j.items():
            print(key ,":", value)
        print("-"*50)
    option_fun()

def email_validate(email):
    if "@" in email:
        user = email.split("@")
        if "." in user[1]:
            return True
        else:
            return False

    else:
        return False
    
option = 0

def option_fun():
    global option
    option = int(input("""
                    Enter a number from 1 to 5 only.
                    1 : add number
                    2 : search
                    3 : update
                    4 : delete
                    5 : list all contacts
                    6 : Exit
                    """))
    

    if option == 1 :
        add()

    elif option == 2:
        search()

    elif option == 3:
        update()

    elif option == 4:
        delete()

    elif option == 5 :
        list_all_contact()

    elif option == 6:
        print("Thanks for using contact")
        exit

    else:
        print("You entered wrong input. Plz try again")
        option_fun()


option_fun()
