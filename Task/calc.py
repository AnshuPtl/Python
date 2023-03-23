#Calc

class Calc:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    
    def add(self):
        return self.num1+self.num2

    def sub(self):
        return self.num1-self.num2

    def mul(self):
        return self.num1*self.num2

    def div(self):
        return self.num1/self.num2

    def expo(self):
        return self.num1**self.num2


a=Calc(10,2)

print("Addition of vlaues: ",a.add())
print("Substraction of vlaues: ",a.sub())
print("Multiplication of vlaues: ",a.mul())
print("Division of vlaues: ",a.div())
print("Exponentiation of value: ",a.expo())
