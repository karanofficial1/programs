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