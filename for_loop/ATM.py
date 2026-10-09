
balance = 50000.0
pin = 1234
attempt = 3
print("Welcome To Our ATM")

while attempt >0 :
    user_pin = int(input("Enter your pin number: "))
    if pin == user_pin:
        while True:
            option = input ('''
                        Please Enter 
                        1 for balance inquiry
                        2 for withdraw
                        3 for deposit
                        4 change pin
                        5 exit
                        ''')
            if option=="1":
                print("your balance is Rs. {}".format(balance))
                break
            elif option=="2":
                withdraw = float(input("Enter your withdraw amount (only in multiple of 500/1000) :"))
                if withdraw > balance:
                    print("Insufficient Balance.")
                    break
                else:
                    if withdraw % 500 == 0:
                        balance -= withdraw
                        print("You have withdraw Rs. {} ".format(withdraw))
                        print("Your remaining balance is Rs. {} ".format(balance))
                        break
                    else:
                        print("Please Enter valid amount in multiple of 500/1000. ")
                        break
                    
            elif option=="3":
                deposit = float(input("Enter your deposit amount: "))
                if deposit < 1:
                    print("You cannot deposit less than Rs.0")
                    print("Please Try again")
                    break
                else:
                    balance += deposit
                    print("You have deposit Rs. {} ".format(deposit))
                    print("Your remaining balance is Rs. {} ".format(balance))
                    break

            elif option=="4":
                new_pin = int(input("Enter your new pin: "))
                confirm_new_pin = int(input("Re-enter your new pin: "))
                if new_pin == confirm_new_pin:
                    pin = new_pin
                    print("Your pin has been changed successfully.")
                else:
                    print("Sorry! please Try again.")
                break
            elif option == "5":
                print("Thanks for using our ATM.")
                break
            else:
                print("Your Entered Wrong Input. Please try again.")
                break       
    else:
        print("Please enter your correct pin.")    
        attempt -=1
        print("You have {} attempt left. Please use correct pin else your account will be blocked.".format(attempt))
else:
    print("your ATM has been blocked. Please Contact Bank to activate.")
        

    
    
