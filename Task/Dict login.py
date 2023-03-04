d1={
    'Name':'User',
    "E-mail":"user@gmail.com",
    'Pswd':'user123'
    }

username=input("Enter username/email id: ")
pswd=input("Enter Password: ")

if username==d1['E-mail'] and pswd==d1['Pswd']:
    print("Login Success")
else:
    print("Acess Denied")
    
print('==============================================')

d={}


username=input("Enter username/email id: ")
pswd=input("Enter Password: ")

while len(pswd)<=7:
    print("The Password must be more than 8 characters required")
    username=input("Enter username/email id: ")
    pswd=input("Enter Password: ")

else:
    d["Username"]=username
    d['pswd']=pswd
    print(d)
