#User details with Encapsulation

class User:

    def name(self,x):
        self.name=x
        
    def age(self,x):
        self.age=x

    def Gender(self,x):
        self.gender=x

    def Email(self,x):
        self.email=x

    def Address(self,x):
        self.address=x
        
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        print("E-Mail: ",self.email)
        print("Address: ",self.address)

u=User()

u.name(input("Enter your name: "))
u.age(int(input("Enter your age: ")))
u.Gender(input("Enter your Gender: "))
u.Email(input("Enter your E-Mail: "))
u.Address(input("Enter your Address: "))

print("============================User============================")

u.display()
    
