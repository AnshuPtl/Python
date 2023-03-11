#Append = Add elements into list

l1=[]

for i in range(1,6):
    n=int(input("Enter Number:"))
    l1.append(n)
print(l1)


#Extend = Add list elements in another list

l2=['Apple','Orange']

l1.extend(l2)
print(l1)
