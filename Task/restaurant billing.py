
def total(q,p):
    return q*p


l1=['Srno.',1,2,3,4]
l2=['Item',"Pizza","Burger","Pani-Puri","Dosa"]
l3=['Price','90/-','89/-','100/-','80/-']
l4=['price',90,89,100,80]

d=dict(zip(l1,l2))

d1=dict(zip(l1,l4))


print("=======================Welcome to Tops Restaurant=======================")

z1=zip(l1,l2,l3)
pizz=0
burg=0
pani=0
dosa=0


for i,j,k in z1:
    print(i," ",j," ",k)

chs=True
while chs:
    n = int(input("Enter Your Choice: "))
    if n == 1:
        print("Your item: ",d.get(n))
        q = int(input("Enter Quantity: "))
        pizz=total(q,d1.get(n))
        print("Total Price: ",pizz)

    elif n == 2:
        print("Your item: ",d.get(n))
        q = int(input("Enter Quantity: "))
        burg=total(q,d1.get(n))
        print("Total Price: ",burg)

    
    elif n == 3:
        print("Your item: ",d.get(n))
        q = int(input("Enter Quantity: "))
        pani=total(q,d1.get(n))
        print("Total Price: ",pani)

    
    elif n == 4:
        print("Your item: ",d.get(n))
        q = int(input("Enter Quantity: "))
        dosa=total(q,d1.get(n))
        print("Total Price: ",dosa)

        
    choice = input ("DO you want to continue: ['Y/N']")
    if choice!='y':
        chs = False


print("==========================Thank You==========================")


total_bill = pizz+burg+pani+dosa
print("Your Total Bill: ",total_bill)
    


    
