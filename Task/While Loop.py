#WAP for while loop
status = True
while status:
    num=int(input("Enter Number: "))

    choice = input ("DO you want to continue: ['Y/N']")

    if choice!='y':
        status = False
