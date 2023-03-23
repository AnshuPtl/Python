#Tours & Travels

class City():
    def cityname(self):
        d={1:'Ahmedabad',2:"Rajkot",3:'Patan',4:'Gandhinagar',5:"Surat"}
        for i,j in d.items():
            print(i,'.',j)

class Signup():
    def name(self):
        name=input("Enter your Name: ")
        return name

    def gender(self):
        gender=input("Enter your Gender: ")
        return gender
    
    def email(self):
        email=input("Enter your E-mail: ")
        return email

    def pswd(self):
        pswd=input("Enter your Password: ")
        return pswd
    

class Login(City,Signup):
    def emaildata(self):
        emaildata=input("Enter your E-mail: ")
        return emaildata
    def pswddata(self):
        pswddata=input("Enter your Password: ")
        return pswddata

    
user={}
userl={}


print("-------------------------Welcome to Tours & Travels-------------------------")

l=Login()

l.cityname()

choice=input("Do you want to register: [y/n]? : ")

if choice=='y':
    print('=========================================================')
    print("Welcome to Registration")
    user['name']=l.name()
    user["gender"]=l.gender()
    user['email']=l.email()
    user["pswd"]=l.pswd()
    print(user)
        
    print('')
    print("Registration done sucessfully")

    choice1=input("Do you want to login: [y/n]? : ")

    if choice1=='y':
        print('=========================================================')
        print("Welcome to Login")
        userl['email']=l.emaildata()
        userl["pswd"]=l.pswddata()

        if userl.get('email') == user.get('email'):
            if userl.get('pswd') == user.get('pswd'):
                print("Login Successful")
            else:
                print("Access Denied")
        else:
            print("Access Denied")

    else:
        print("Thank You")
        exit

else:
    print("Thank You")
    exit

