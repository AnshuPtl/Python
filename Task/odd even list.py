#WAP for Even & Odd numbers from list

l1=[]
for i in range(0,10):
    n = int(input("Enter Number: "))
    l1.append(n)

even = []
odd = []

for n in l1:
    if n%2==0:
        even+=[n]
    else:
        odd+=[n]
print("Even Numbers:",even)
print('Odd Numbers:',odd)
