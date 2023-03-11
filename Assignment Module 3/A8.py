#Write a Python program to remove duplicates from a list.

l1=[1,2,3,45,6,3,1,50,8,45]

l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)
