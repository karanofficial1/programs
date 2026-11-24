# init function Constructor



# class Student:
#     name = "Karan"

#     def __init__(self):
#         print(self)
#         print("Adding new student...")


# s1 = Student()


# s2 = Student()
# print(s2.name)








class Student:

    school_name = "ABC School"
    fullname = 'Pratik'

    #default constructors
    def __init__():
        print("Hello my name is karan")

    #parameterized constructors
    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age = age
        print(f"Adding new student... {self.fullname} and age is {self.age}")

    def Welcome(self):
        return f"Welcome {self.fullname} "

s1 = Student('karan',25)
print(s1.fullname, "-", s1.age)
print(s1.school_name)
print(Student.school_name)
print(s1.fullname)
print(Student.fullname)
print(s1.Welcome())




class Person:
  def __init__(self, name= "Pratik", age = 25):
    self.name = name
    self.age = age

p1 = Person("Karan", 25)

print(p1.name)
print(p1.age)
print("Hello my name is", p1.name)

p2 = Person()
print("Hello my name is", p2.name)
