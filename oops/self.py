class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name, "And my age is :", self.age)

    def welcome(self):
        message = self.greet()
        return message

p1 = Person("Karan", 30)
p1.greet()

p1.welcome()

