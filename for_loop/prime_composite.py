number = int(input("Enter a number: "))
prime = False
if number == 2:
    prime= True
for i in range(2, number):
    if number % i == 0:
        print("Composite")
        prime = False
        break
    else:
        prime = True

if prime:
    print("Prime number")


# if number == 2:
#     print("ODd number.")   

# for i in range(3, number):
#     if number % i == 0:
#         print("Composite number.")
#         break
#     else:
#         print("Odd number")   
