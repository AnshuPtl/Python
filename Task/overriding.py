#Method OverRiding : Runtime Polymorphism

class A:
    def display(self,var1):
        print("Value of var1: ",var1)

class B(A):
    def display(self,a1,a2):
        return a1*a2

obj = B()
print(obj.display(23,5))
