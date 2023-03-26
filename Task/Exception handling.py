#Exception handling

try:
    n1=int(input("Enter Num1: "))
    n2=int(input("Enter Num2: "))

    div = n1/n2

    print("Division: ",div)
    print(name)

except NameError as n:
    print("Error: ",n)

except ZeroDivisionError as z:
    print("Error: ",z)


print("=========================================================")

try:
    n = int(input("Enter marks:"))

    assert n>=40

except:
    print("Fail")

else:
    print("Pass")
    
finally:
    print("This is a finally Block")
