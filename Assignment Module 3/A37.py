#How Do You Check The Presence Of A Key In A Dictionary?

def check(d, i):
    if i in d.keys():
        print("Key already exists in the dictionary")
    else:
        print("Key does not exist in the dictionary")


d={1:"ABC",2:"XYZ",3:"PQR"}
n=int(input("Enter a key:"))

print(check(d,n))

print(d.get(n))
