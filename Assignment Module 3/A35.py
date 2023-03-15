#Write a Python script to check if a given key already exists in a dictionary.
def check(dict, key):
    if key in dict.keys():
        print("Key already exists in the dictionary")
    else:
        print("Key does not exist in the dictionary")

        
d = {1:'a', 2:'b', 3:'c'}

n= int(input("Enter a num:"))

print(check(d,n))
        
