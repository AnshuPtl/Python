#Method OverLoading : Compiletime Polymorphism

class A:
    def __init__(self,a):
        self.num=a

    def __add__(self,b):
        return self.num+b.num

op1 = A(12)
op2 = A(3)

op3 = op1+op2

print("Addition of two object values: ",op3)


class B:
    def display(a,b):
        return a*b
    def display(a,b,c):
        return a*b*c

obj = B()

print(obj.display(4,5,5))
