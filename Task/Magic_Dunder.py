#Magic / Dunder Methods

class Sample():
    def __init__(self,x):
        self.num=x

    def display(self):
        print("Value: ",self.num)

a=Sample(125)
b=Sample(111)
b.display()
a.display()



class Sample2():
    def __str__(self):
        return "Your name is: "+self.namex

    def __init__(self,name):
        self.namex=name

a=Sample2("ABC")
print(a)
