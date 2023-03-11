#Area Finder

d={1:'Circle',2:'Triangle',3:'Rectangle'}

def circle(r):
    
    return 3.14*r*r


def triangle(b,h):
    
   return 1/2*b*h


def rectangle(hi,w):
    return hi*w



print("====================Area Finder====================")

for i,j in d.items():
    print(i,':',j)

choice=int(input("Please choose a option:"))

if choice==1:
    radius = int(input("Enter Radius: "))
    print("Area of circle is:",circle(radius))
    print("====================Thank You====================")


elif choice==2:
    base = int(input("Enter Base: "))
    hight = int(input("Enter Height: "))
    print("Area of Triangle is:",triangle(base,hight))
    print("====================Thank You====================")

elif choice==3:
    hight = int(input("Enter Height: "))
    width = int(input("Enter Width: "))
    print("Area of Rectangle is: ",rectangle(hight,width))
    print("====================Thank You====================")

else:
    print("Please enter a valid input")





