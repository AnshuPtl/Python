#Write a Python function that takes a list and returns a new list with unique elements of the first list.

l=[]

for i in range(1,6):
    n= int(input("Enter Elements:"))
    l.append(n)
print(l)

l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)
    
    
