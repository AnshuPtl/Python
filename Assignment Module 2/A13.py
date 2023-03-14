#Write a Python program to count the number of characters (character frequency) in a string

a={}
s="HelloWorldPython"

for i in s:
    if i in a:
        a[i]+=1
    else:
        a[i]=1

print("The number of characters:"+str(a))
