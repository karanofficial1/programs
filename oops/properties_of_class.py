class Person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

p1 = Person("Karan", 25, "male")
print(p1.age)

p1.age = 30
print(p1.age)
print(p1.sex)
del p1.sex  # deleting sex
# print(p1.sex)  # Attribute Error: Person object has no attribute sex -- if this code is run
p1.city = "Mahendranagar"
print(p1.city)


class Calculator:
    def add(self,a,b):
        return a + b

    def mul(self, a,b):
        return a * b

cal = Calculator()
print(cal.add(5,4))

print(cal.mul(5,4))



