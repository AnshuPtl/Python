#WAP to create registration Form using tkinter
from tkinter import *
import tkinter.messagebox as msg

d={}
d1={}

def show():
    for i,j in d.items():
        print(i,":",j)
def insert():
    if fn.get()=="" or ln.get()=="" or e.get()=="" or c.get()=="" or var.get()=="" or a.get()=="" or ad.get()=="":
        msg.showinfo("Alert","All fields are mandatory!!!")
    else:
        d['FirstName']=fn.get()
        d["LastName"]=ln.get()
        d['E-mail']=e.get()
        d["Contact"]=c.get()
        d['Gender']=var.get()
        d['Age']=a.get()
        d['Address']=ad.get()
        print(d)
        msg.showinfo("User Details","First Name: "+fn.get()+"\nLast Name: "+ln.get()+"\nE-mail: "+e.get()+"\nContact: "+c.get()+"\nGender: "+var.get()+"\nAge: "+a.get()+"\nAddress: "+ad.get())
        

def update():
    if fn.get()=="" or ln.get()=="" or e.get()=="" or c.get()=="" or var.get()=="" or a.get()=="" or ad.get()=="":
        msg.showinfo("Alert","All fields are mandatory!!!")
    else:
        d1['FirstName']=fn.get()
        d1["LastName"]=ln.get()
        d1['E-mail']=e.get()
        d1["Contact"]=c.get()
        d1['Gender']=var.get()
        d1['Age']=a.get()
        d1['Address']=ad.get()
        print(d1)

        d.update(d1)
        print(d)
        msg.showinfo("Updated Data","First Name: "+fn.get()+"\nLast Name: "+ln.get()+"\nE-mail: "+e.get()+"\nContact: "+c.get()+"\nGender: "+var.get()+"\nAge: "+a.get()+"\nAddress: "+ad.get())

def delete():
    if fn.get()=="" or ln.get()=="" or e.get()=="" or c.get()=="" or var.get()=="" or a.get()=="" or ad.get()=="":
        msg.showinfo("Alert","All fields are mandatory!!!")
    else:
        d.clear()
        print(d)
        msg.showinfo("Alert","User data deleted Successfully")

def search():
    if fn.get() in d.values() or ln.get() in d.values() or e.get()in d.values() or c.get() in d.values()or var.get()in d.values() or a.get() in d.values() or ad.get() in d.values():
        msg.showinfo("User Found",show())
    else:
        msg.showinfo("User not Found","Please register")

def reset():
    if fn.get()=="" or ln.get()=="" or e.get()=="" or c.get()=="" or var.get()=="" or a.get()=="" or ad.get()=="":
        msg.showinfo("Alert","All fields are mandatory!!!")
    else:
        msg.showinfo("User Details","First Name:\nLast Name:\nE-mail:\nContact:\nGender:\nAge:\nAddress: ")


root=Tk()
root.title("Application")
root.geometry('750x750')

fname = Label(root,text="Enter your First Name:")
fname.place(x=25,y=25)

lname = Label(root,text="Enter your Last Name:")
lname.place(x=25,y=50)

email = Label(root,text="Enter your E-mail:")
email.place(x=25,y=75)

contact = Label(root,text="Enter your Contact:")
contact.place(x=25,y=100)

gender = Label(root,text="Enter your Gender:")
gender.place(x=25,y=125)

age = Label(root,text="Enter your Age:")
age.place(x=25,y=150)

address = Label(root,text="Enter your Address:")
address.place(x=25,y=175)


var = StringVar()
fn=Entry(root)
fn.place(x=155,y=26)

ln=Entry(root)
ln.place(x=155,y=51)

e=Entry(root)
e.place(x=155,y=76)

c=Entry(root)
c.place(x=155,y=101)

g=Radiobutton(root,text="Male",variable=var,value="Male")
g.place(x=150,y=125)

g=Radiobutton(root,text="Female",variable=var,value="Female")
g.place(x=200,y=125)

a=Entry(root)
a.place(x=155,y=151)

ad=Entry(root)
ad.place(x=155,y=176)


ibtn = Button(root,text="Insert",font=("Arial 11"),foreground="white",background="Black",command=insert)
ibtn.place(x=125,y=225)

ubtn = Button(root,text="Update",font=("Arial 11"),foreground="white",background="Black",command=update)
ubtn.place(x=325,y=25)

dbtn = Button(root,text="Delete",font=("Arial 11"),foreground="white",background="Black",command=delete)
dbtn.place(x=325,y=75)

sbtn = Button(root,text="Search",font=("Arial 11"),foreground="white",background="Black",command=search)
sbtn.place(x=325,y=125)

rbtn = Button(root,text="Reset",font=("Arial 11"),foreground="white",background="Black",command=reset)
rbtn.place(x=325,y=175)









