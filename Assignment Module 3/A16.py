#Write a Python program to get unique values from a list

l1=[1,2,5,9,5,4,3,80,2,98,75,9,60,1,54]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l1)
print("Unique values from list:",l2)
