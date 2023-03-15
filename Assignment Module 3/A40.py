#Write a Python script to merge two Python dictionaries

d1 = {1:'a', 2:'b'}
d2 = {3:'c', 4:'d'}

merge = {**d1, **d2}

print(merge)
