#Encapsulation / Data Binding

class Sample():
    def input (self, x):
        self.num=x

    def display(self):
        print("Value: ",self.num)

obj=Sample()

obj.input(12)

obj.display()
