import random

user = input("""
            Enter Any choices:
            S --> for Scisor
            P --> for Paper
            R --> fir Rock 

            🪨 Rock beats ✂️ Scissors
            ✂️ Scissors beats 📄 Paper
            📄 Paper beats 🪨 Rock
            """).upper()
print("=" *70)
rand = random.choice(['S','P','R'])
print("user : ", user, "computer : ", rand)
if user not in ['S', 'P', 'R']:
    print("You entered a wrong choice. Please reenter the choice.")
elif (user == "S" and rand == "P") or (user == "R" and rand == "S") or (user =="P" and rand =="R"):
    print("Congratulatios !!! YOU WIN")
elif user == rand:
    print("Draw!!!")
else:
    print("You Lost!!! Computer Win")


