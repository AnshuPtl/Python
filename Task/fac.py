"""num= int(input("Enter number:"))

a=1
for i in range(1,num + 1):
    a = a*i

print(a)


print("==================================================")
a=0
for i in range (1,11):
    a+=i
print(a)
print("==================================================")

for i in range (1,36,3):
    print(i,end=" ")
print("")

for i in range (2,36,3):
    print(i,end=" ")
print("")

for i in range (3,37,3):
    print(i,end=" ")
print("")
print("==================================================")
a=0
for i in range(1,11):
    n=int(input("Enter number "+str(i)+" : "))
    a+=n
print(a)"""

print("==================================================")
for i in range(1,4):
    n=int(input("Enter number "+str(i)+" : "))
    
if i%2==0:
    print("Even numbers are: ",n)
        
        
else:
    print("Odd numbers are: ",n)
