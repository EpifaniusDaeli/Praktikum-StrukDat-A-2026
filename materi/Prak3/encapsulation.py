class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age 

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age)