num=int(input("Enter number: "))

n=num-1+num-2
print(n)


n1=0
n2=1
for i in range(n):
    print(n1)
    n=n1+n2
    n1=n2
    n2=n

