for i in range (1,6):
    for j in range (1,6):
        if (i==5) and (j==4):
            print("$",end="")
        print("*",end="")
    print()

for i in range (1,6):
    for j in range (1,6):
        if(j<=i):
            print("*",end="")
        else:
            print(" ",end="")
    print()


for i in range (1,6):
    for j in range (1,6):
        if(j<=i):
            if(i%2 ==0):
                print("1",end="")
            else:
                print("0",end="")
        else:
            print(" ",end="")
    print()

print("---------------------------------------------")

n = int(input("ENter Number : "))
for i in range (1,n+1):
    print("*"*i+" "*(n-i))

n = int(input("ENter Number : "))
for i in range (1,n+1):
    print(" "*(n-i)+"*"*i)
    
print("---------------------------------------------")
n = int(input("ENter Number : "))
for i in range (1,n+1):
    print(" "*(n-i)+"* "*i)
print("---------------------------------------------")

n = int(input("ENter Number : "))
for i in range (1,n+1):
    print("* "*(n-i)+" "*i)

print("---------------------------------------------")
a = int(input("Enter number: "))

for k in range(a, 1, -1):
    for space in range(0, a-k):
        print("  ", end=" ")
    for l in range(i, 2*k-1):
        print("* ", end="")
    for l in range(1, k-1):
        print("* ", end=" ")
    print("")
    
print("---------------------------------------------")
a = int(input("Enter number: "))  
k = 2 * a - 2  
for i in range(0, a):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 1  
    for j in range(0, i + 1):  
        print("* ", end="")  
    print(" ")  
k = a - 2  
for i in range(a, -1, -1):  
    for j in range(k, 0, -1):  
        print(end=" ")  
    k = k + 1  
    for j in range(0, i + 1):  
        print("* ", end="")  
    print("")
    
print("---------------------------------------------")
a = int(input("Enter number: "))  
for i in range(0, a):  
    for j in range(0, i + 1):  
        print("*", end=' ')  
    print(" ")  
for i in range(a + 1, 0, -1):  
    for j in range(0, i - 1):  
      print("*", end=" ")  
    print(" ")
    
print("---------------------------------------------")    
a = int(input("Enter number: "))
n = 1
for i in range(1, a+1):
    for j in range(1, i+1):
        print(n, end=" ")
        n += 1
    print()
    
