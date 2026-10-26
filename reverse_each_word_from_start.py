string = "Hello i have 25 orange And 15 mangoes."

for char in string[::-1]:
    print(char[::-1], end="") 



print("\n")
for char in string.split():  
    print(char[::-1], end=" ")

