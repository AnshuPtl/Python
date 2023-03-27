#Calculator in tkinter

from tkinter import *
import tkinter.messagebox as msg

def add():
    if e1.get()=="" or e2.get()== "":
        msg.showinfo("Alert","Number1 and Number2 are Mandatory!!!")
    else:
        msg.showinfo("Addition:",int(e1.get())+int(e2.get()))

def sub():
    if e1.get()=="" or e2.get()=="":
        msg.showinfo("Alert","Number1 and Number2 are mandatory!!!")
    else:
        msg.showinfo("Substraction:",int(e1.get())-int(e2.get()))

def mul():
    if e1.get()=="" or e2.get()== "":
        msg.showinfo("Alert","Number1 and Number2 are Mandatory!!!")
    else:
        msg.showinfo("Multiplication:",int(e1.get())*int(e2.get()))

def div():
    if e1.get()=="" or e2.get()=="":
        msg.showinfo("Alert","Number1 and Number2 are mandatory!!!")
    else:
        msg.showinfo("Division:",int(e1.get())/int(e2.get()))

def expo():
    if e1.get()=="" or e2.get()== "":
        msg.showinfo("Alert","Num1 and Num2 are Mandatory!!!")
    else:
        msg.showinfo("Exponential:",int(e1.get())**int(e2.get()))
        

root=Tk()
root.title("Calculator")
root.geometry("500x500")

num1=Label(root,text="Enter Number 1:")
num1.place(x=10,y=10)

num2=Label(root,text="Enter Number 2:")
num2.place(x=10,y=50)

e1=Entry(root)
e1.place(x=105,y=11.3)

e2=Entry(root)
e2.place(x=105,y=51.3)

abtn = Button(root,text="Add",font=("Ariel 10"),foreground="white",background="blue",command=add)
abtn.place(x=50,y=100)

sbtn = Button(root,text="Sub",font=("Ariel 10"),foreground="white",background="blue",command=sub)
sbtn.place(x=150,y=100)

mbtn = Button(root,text="Mul",font=("Ariel 10"),foreground="white",background="blue",command=mul)
mbtn.place(x=50,y=200)

dbtn = Button(root,text="Div",font=("Ariel 10"),foreground="white",background="blue",command=div)
dbtn.place(x=150,y=200)

ebtn = Button(root,text="Expo",font=("Ariel 10"),foreground="white",background="blue",command=expo)
ebtn.place(x=100,y=150)
