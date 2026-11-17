fruit = ['apple', 'banana', 'mango']
fruit[1:2] = ['orange', 'grapes']
print(fruit)  


print(-5**2)    


a  = 5 
b = 10
if a < b :
    a = a + b
print(a, b)

if a > b :
    b = b + 2

print(a, b)

num = [10,20,30,40]
num.remove(20)
a= num.pop() # remove 40 from list and return the removed list
print(a)
del num[0]
print(num)



#
sum = 0
def Karan(*args):
    for i in args:
        global sum
        sum += i


Karan(5,10,15,20)
print(sum)

#Write a program which takes a sequence of numbers and check if all numbers are unique using set.
def check_distinct(data_list):
    if len(data_list) == len(set(data_list)):
        return True
    else:
        return False;
print(check_distinct([1,6,5,8]))     #Prints True
print(check_distinct([2,2,5,7,8]))   #Prints False



a = 5
b = a
a += 5
print(a, b)



a = [1,2,3]
b = a
a.pop()
print(a)
print(b)