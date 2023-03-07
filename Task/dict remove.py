#Dictionary elements remove

d=dict(name="python",age=12,DOB='11/11/2011',vehicle='car')

print(d)

d.pop('age')
print(d)

d.popitem()
print(d)

del d['DOB']
print(d)

d.clear()
print(d)

del d
print(d)
