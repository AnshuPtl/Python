#Abstraction

class RBI:
    def interest(self):
        pass

class SBI(RBI):
    def interest(self):
        print("We offer 7% interest on home loan")

class HDFC(RBI):
    def interest(self):
        print("We offer 8% interest on home loan")

class Axis(RBI):
    def interest(self):
        print("We offer 10% interest on home loan")

b1=SBI()
b2=HDFC()
b3=Axis()

b1.interest()
b2.interest()
b3.interest()
