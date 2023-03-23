#1.Public
#2.Private
#3.Protected

print("===========================Public===========================")
class Bird:
    def __init__(self):
        self.name="Eagle"
        self.age=2

    def display(self):
        print("Name of bird: ",self.name)
        print("Age of Bird: ",self.age)

b = Bird()
b.display()
print("out of class name: ",b.name)
print("out of class age: ",b.age)

print("===========================Private===========================")

class Bird:
    def __init__(self):
        self.__name="Eagle"
        self.age=2

    def display(self):
        print("Name of bird: ",self.__name)
        print("Age of Bird: ",self.age)

b = Bird()
b.display()
print("out of class name: ",b._Bird__name)
print("out of class age: ",b.age)
