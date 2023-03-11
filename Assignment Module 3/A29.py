#WAP  to remove an empty tuple(s) from a list of tuples.

l=[(1,8),(5,8,3,9),(),(9,0,7,11),(20,8,95),()]

print(l)

for i in l:
    if len(i)==0:
        l.remove(i)
print("After removing an empty tuples from list:",l)
