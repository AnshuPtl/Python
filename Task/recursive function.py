#Recursive Function:

n=int(input("Enter a number to find factorial: "))

def factorial(x):
    if x<=0:
        return 1
    else:
        return x*factorial(x-1)

print(f"factorial of {n} is : ",factorial(n))

print("=======================================================")

num=int(input("Enter a number to find Addition of all natural numbers: "))

def add(a):
    if a<=0:
        return 0
    else:
        return a+add(a-1)

print(f"Addition of {num} is : ",add(num))
