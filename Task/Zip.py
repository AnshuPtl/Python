#Zip

l1=[1,2,3,4,5]
l2=['a','b','c','d']
l3=["One","Two","Three","Four"]

print(list(zip(l1,l2,l3)))

z1=zip(l1,l2,l3)
print(list(z1))


#Unzip

a,b = zip(*z1)

print(a)
print(b)
