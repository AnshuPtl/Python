
def disc(t,d):
    return t*d/100

def price(t,d):
    return t-d

name=input("Enter your name: ")

age=int(input("Enter your age: "))

citizenship=input("Enter your citizenship: ")

Total_price=int(input("Enter Total purchase price: "))

if citizenship == 'indian':
    if Total_price>=500:
        if age>=18 and age<=40:
            print("Total Price: ",Total_price)
            print("Dicounted Amount: ",disc(Total_price,30))
            print("Final price after applying the discount: ",price(Total_price,disc(Total_price,30)))

if citizenship == 'indian':
    if Total_price>5000:
        if age>40:
            print("Total Price: ",Total_price)
            print("Dicounted Amount: ",disc(Total_price,50))
            print("Final price after applying the discount: ",price(Total_price,disc(Total_price,50)))
    
