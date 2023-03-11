#choice board

d={1:'Addition',2:'Substaction',3:'Multiplication',4:'Division',5:'Modulo',6:'Exit'}

def add(a,b):
    
    return a+b

def sub(a,b):
    
    return a-b

def mul(a,b):
    
    return a*b

def div(a,b):
    
    return a/b

def mod(a,b):
    
    return a%b

def choic(inp):
    print(d.get(inp))

    

print("=====================Choice Board=====================")



con=True
while con:
    for i,j in d.items():
        print(i,".",j)
    choice=int(input("Enter your choice:"))
    if choice == 1:
        print("your choice is: ",d.get(choice))
        n1=int(input("Enter num1:"))
        n2=int(input("Enter num2:"))
        print(n1,'+',n2,'=',add(n1,n2))
        choice2=input("Do you want to continue: ['Y/N']")
        if choice2!='y':
            con=False
            
    elif choice==2:
        print("your choice is: ",d.get(choice))
        n1=int(input("Enter num1:"))
        n2=int(input("Enter num2:"))
        print(n1,'-',n2,'=',sub(n1,n2))
        choice2=input("Do you want to continue: ['Y/N']")
        if choice2!='y':
            con=False

    elif choice==3:
        print("your choice is: ",d.get(choice))
        n1=int(input("Enter num1:"))
        n2=int(input("Enter num2:"))
        print(n1,'*',n2,'=',mul(n1,n2))
        choice2=input("Do you want to continue: ['Y/N']")
        if choice2!='y':
            con=False

    elif choice==4:
        print("your choice is: ",d.get(choice))
        n1=int(input("Enter num1:"))
        n2=int(input("Enter num2:"))
        print(n1,'/',n2,'=',div(n1,n2))
        choice2=input("Do you want to continue: ['Y/N']")
        if choice2!='y':
            con=False

    elif choice==5:
        print("your choice is: ",d.get(choice))
        n1=int(input("Enter num1:"))
        n2=int(input("Enter num2:"))
        print(n1,'%',n2,'=',mod(n1,n2))
        choice2=input("Do you want to continue: ['Y/N']")
        if choice2!='y':
            con=False

    elif choice==6:
        print("your choice is: ",d.get(choice))
        ext=True
        while ext:
            choice3=input("Are you sure to exit: ['Y/N']")

            if choice3!='y':
                ext=False
            else:
                quit()
else:
    print("Thank You")
