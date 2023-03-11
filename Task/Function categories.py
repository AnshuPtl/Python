#Without return value without parameter/argument

def display():
    print("This is a display function")
display()

print("=================================================")

#Without return value with parameter/argument

num=11
def display(a,b):
    print("Value of a: ",a)
    print("Value of b: ",b)
    print("Value of num: ",num)
    print("Addition of a&b is:",a+b)
display(50,81)


print("=================================================")

#With return value without parameter/argument

def add():
    n1=int(input("Enter num1:"))
    n2=int(input("Enter num2:"))

    return n1+n2
print("Addition of two values is:",add())


print("=================================================")

#With return value with parameter/argument

def add(a,b):
    
    return a+b

n1=int(input("Enter num1:"))
n2=int(input("Enter num2:"))
print("Addition of two values is:",add(n1,n2))
