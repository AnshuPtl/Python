# Class


class Sample:
    a=11

obj = Sample()
obj2=Sample()

print("Value of a: ",obj.a)
obj.a = 25

print("Manipulated value of a: ",obj.a)

print("Value of a using obj2: ",obj2.a)


# user input in class

class ABC:
    def display(self,x):
        print("You have Entered: ",x)

a=ABC()

val=int(input("Your number: "))

a.display(val)
