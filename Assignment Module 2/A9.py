#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
c=int(input("Enter num3: "))



if a == b or b == c or a == c:
    ans=0
else:
    ans = a+b+c

print("Sum of values: ",ans)

