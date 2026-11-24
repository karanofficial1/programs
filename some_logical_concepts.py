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


# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
non_negative = [i for i in numbers if i >= 0 ]
print(non_negative)

square = [i*i for i in numbers]    # square numbers of above list
print(square)

## Filter only negative and zero in the list using list comprehension and make their square
non_negative = [i*i for i in numbers if i >= 0 ]
print(non_negative)


# Generating even numbers
even_numbers = [i for i in range(11) if i % 2 == 0]
print(even_numbers)

# Generating odd numbers
odd_numbers = [i for i in range(11) if i % 2 != 0]
print(odd_numbers)

#lambda function
square = lambda x : x ** 2
print(square(3))  

sum = lambda x,y,z : x+y+z
print(sum(3,4,5))

# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [i for j in list_of_lists for i in j]
print(flatten)


# Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

tuple_list= [(i, 1, i, i*i, i*i*i, i*i*i*i, i*i*i*i*i ) for i in range(11)]
print(tuple_list)


# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
new_countries = [[country.upper(), country[:3].upper(), capital.upper()] for [(country, capital)] in countries]
print(new_countries)





countries = [[('Finland', 'Helsinki',"English")], [('Sweden', 'Stockholm',"English")], [('Norway', 'Oslo', "English")], [("nepal", "Kathmandu", "Nepali")]]
new_countries = [[country.upper(), country[:3].upper(), capital.upper(), language.upper()] for [(country, capital, language)] in countries]
print(new_countries)



# change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
new_names = [(name + " " + caste) for [(name, caste)] in names]
print(new_names)



# Change the following list to a list of dictionaries:

countries = [[('Nepal', 'Kathmandu')], [('India', 'Delhi')], [('Japan', 'Tokiyo')]]
new_country = [ {'country' : country.upper(), 'city': capital.upper() } for [(country, capital)] in countries]
print(new_country)

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)                



def sum(*nums):
    total = 0
    for i in nums:
        total += i

    print("Total : ", total)

sum(5,10,15)

def student(class_name, *names):
    print("Class", class_name, "Student names:")
    for name in names:
        print(name.upper())

student(5,"karan", "pratik", "prince", "tara")