#Strings:

s="Hello All"
name="Stark"

print(s+f" My name is: {name}")
print(s+name)
print(s+" My name is: {}".format(name))

n1="Hello have a good day, have happy morning"

print("Occourance of substring is : ",n1.count("have"))

print(n1.swapcase())

pswd='ty78'
print(pswd.isdigit())

s1="Hello"
print(s1.center(10,"*"))
print("Split string: ",s1.split('1'))

print('good' in n1)


#String slicing:

s1="Welcome to Tops Tech"
count=0

#Strings are iterable
for i in s1:
    count+=1

#slice
print(s1[4:11])

sub="ABC"

print(s1[:9]+sub+s1[9:])
