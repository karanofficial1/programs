# Write a Python program that filters names beginning with the letter 'S' or 's' from the given list and stores
# them (all lowercase) in a new list

input  = ['sujan', 'manoj', 'suman', 'raj', 'David', 'Shyam']
store = []

for i in input:
    if (i.startswith("S") or i.startswith("s")):
        store.append(i.lower())
print(store)