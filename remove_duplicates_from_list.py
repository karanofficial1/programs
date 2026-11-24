a = [1,1,2,2,3,3,4,4,4]

remove = []
for i in a:
    if i not in remove:
        remove.append(i)

print(remove)