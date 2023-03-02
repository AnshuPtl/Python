#Remove redundunt data from list

l1=[12,51,20,30.3,4,80,51,30.3,9,15,4]

l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)
