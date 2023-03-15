#Write a Python program to check multiple keys exists in a dictionary

def keys_exist(d, keys):
    for key in keys:
        if key not in d:
            return False
    return True

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys = ['a', 'b', 'e']

if keys_exist(d, keys):
    print("All keys exist in the dictionary")
else:
    print("One or more keys not exists in the dictionary")
