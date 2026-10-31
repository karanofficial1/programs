'''
Review the ATM program written in class, correct its weaknesses and extend it.
REQUIREMENTS
• Prevent withdrawals that exceed the available balance and display a suitable message.
• Keep the menu running until the user selects Exit, instead of ending after one action.
• Store every deposit and withdrawal in a transactions list and add a "Mini Statement" option to display it.
• Restructure the program into functions: check_balance(), withdraw() and deposit().
'''

from datetime import datetime
    
balance = 50000.0
pin = 1234
attempt = 3
transactions = []
print("Welcome To Our ATM")

def deposit(deposit_amount):
    global balance
    if deposit_amount < 1:
        print("You cannot deposit less than Rs.0")
        print("Please Try again")
        
    else:
        balance += deposit_amount
        print("You have deposit Rs. {} ".format(deposit_amount))
        print("Your remaining balance is Rs. {} ".format(balance))
        transactions.append("Deposit:{} at Rs. {}".format(datetime.now() , deposit_amount))  

def withdraw(withdraw_amount):  
    global balance 
    balance -= withdraw_amount
    print("You have withdraw Rs. {} ".format(withdraw_amount))
    print("Your remaining balance is Rs. {} ".format(balance))
    transactions.append("Withdrawl  at : {} Rs. {}".format(datetime.now(), withdraw_amount)) 

def change_pin():
    new_pin = int(input("Enter your new pin: "))
    confirm_new_pin = int(input("Re-enter your new pin: "))
    if new_pin == confirm_new_pin:
        pin = new_pin
        print("Your pin has been changed successfully.")
    else:
        print("Sorry! please Try again.")
    
def check_balance():
    print("your balance is Rs. {}".format(balance))


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
                        5 mini statement
                        6 exit
                        ''')
            if option=="1":
                check_balance()

            elif option=="2":
                withdraw_amount = float(input("Enter your withdraw amount (only in multiple of 500/1000) :"))
                if withdraw_amount > balance:
                    print("Insufficient Balance.")
                else:
                    if withdraw_amount % 500 == 0:
                        withdraw(withdraw_amount)

                    else:
                        print("Please Enter valid amount in multiple of 500/1000. ")
                    
            elif option=="3":
                deposit_amount = float(input("Enter your deposit amount: "))
                deposit(deposit_amount)               

            elif option=="4":
                change_pin()
            
            elif option == "5":
                if transactions:
                    for transaction in transactions:
                        print(transaction)
                else:
                    print("No Transaction till now.")

            elif option == "6":
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
        
