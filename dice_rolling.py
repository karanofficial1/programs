dice = int(input("Enter a number from 1 to 6: "))

import random
rand = random.randint(1,6)

if dice not in [1,2,3,4,5,6]:
    print("Enter a number between 1 and 6 only.")
elif dice > rand:
    print("Congratulations You Win")

elif dice < rand:
    print("Computer wins")
else:
    print("Tie")