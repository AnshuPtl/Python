#Inheritance

print("-------------------Single-------------------")
class Parent:
    def __init__(self,a,b):
        self.n1=a
        self.n2=b

    def add(self):
        return self.n1+self.n2

class Child(Parent):
    def sub(self):
        return self.n1-self.n2

c=Child(11,5)

print("Addition: ",c.add())
print("Substraction: ",c.sub())

print("-------------------Multilevel-------------------")


class A:
    def __init__(self,a,b):
        self.n1=a
        self.n2=b

    def add(self):
        return self.n1+self.n2

class B(A):
    def sub(self):
        return self.n1-self.n2

class C(B):
    def mul(self):
        return self.n1*self.n2

class D(C):
    def div(self):
        return self.n1/self.n2

q=D(10,5)

print("Division: ",q.div())
print("Multiplication: ",q.mul())
print("Addition: ",q.add())
print("Substraction: ",q.sub())

print("-------------------Multiple-------------------")

class A:
    def __init__(self,a,b):
        self.n1=a
        self.n2=b

    def add(self):
        return self.n1+self.n2

class B:
    def sub(self):
        return self.n1-self.n2

class C:
    def mul(self):
        return self.n1*self.n2

class D(A,B,C):
    def div(self):
        return self.n1/self.n2

q=D(10,5)

print("Division: ",q.div())
print("Addition: ",q.add())
print("Substraction: ",q.sub())
print("Multiplication: ",q.mul())

print("-------------------Heriachical-------------------")


class A:
    def __init__(self,a,b):
        self.n1=a
        self.n2=b

    def add(self):
        return self.n1+self.n2

class B(A):
    def sub(self):
        return self.n1-self.n2

class C(A):
    def mul(self):
        return self.n1*self.n2

class D(A):
    def div(self):
        return self.n1/self.n2

q=D(10,5)

print("Division: ",q.div())
print("Addition: ",q.add())


w=C(50,8)
print("Addition: ",w.add())
print("Multiplication: ",w.mul())

r=B(18,10)
print("Addition: ",r.add())
print("Substraction: ",r.sub())



print("-------------------Hybrid-------------------")


class A:
    def __init__(self,a,b):
        self.n1=a
        self.n2=b

    def add(self):
        return self.n1+self.n2

class B(A):
    def sub(self):
        return self.n1-self.n2

class C(A):
    def mul(self):
        return self.n1*self.n2

class D(B,C):
    def div(self):
        return self.n1/self.n2

q=D(10,5)

print("Division: ",q.div())
print("Substraction: ",q.sub())
print("Multiplication: ",q.mul())
print("Addition: ",q.add())








