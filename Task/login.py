d1={}

user=input("Enter username/email id:")
pswd=input("Enter Password:")

while len(pswd)<=7:
    print("The password must be more than 8 letters required")
    user=input("Enter username/email id:")
    pswd=input("Enter Password:")

else:
    d1['user']=user
    d1['pswd']=pswd
    print(d1)
print("Please login to the account")
user=input("Enter username/email id:")
pswd=input("Enter Password:")

if user==d1['user'] and d1['pswd']:
    print("Login Success")
else:
    print("Invalid username or password")
