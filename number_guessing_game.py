import random
print("Number Guessing Game:")
print("="*70)

rand = random.randint(1,10)
print(rand)
while True:
    num = int(input("Enter a number from 1 to 10: "))
    if num>10:
        print("Your number is greater than 100")
    elif num<1:
        print("your number is less than 1")
    elif num == rand:
        print("Congratulations! You are correct.")
        break
    elif num > rand:
        print("Too High")
    else:
        print("Too Low")
        
print("Game Over")
  