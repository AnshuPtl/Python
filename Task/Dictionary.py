#Dictionary
d1={
    "Key":'Value',
    "Key1":11
    }
print(type(d1))

print('==============================================')

l1=[(58,11),(33,50)]
d1=dict(l1)
print(type(d1))
print(d1)

print('==============================================')

d={
    1:'One',
    2:"Two",
    3:'Three'
    }
for i in d:
    print(i)

print('==============================================')

for i in d.keys():
    print(i)


print('==============================================')

for i in d.values():
    print(i)

print('==============================================')

for i in d.items():
    print(i)

print('==============================================')

for k,v in d.items():
    print(k,v)


print('==============================================')

d1={
    1:'One',
    2:"Two",
    3:'Three'
    }
d2={
    4:'Four',
    2:"New Two",
    3:'New Three'
    }
d1.update(d2)
print(d1)
