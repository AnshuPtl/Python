#WAP to add two numbers using tkinter gui

from tkinter import *
import tkinter.messagebox as msg

root=Tk()
root.title("My Tkinter")
root.geometry("500x500")

#var = StringVar() : it represents string value

var = IntVar() #It represent Integer Value

def display():
    msg.showinfo("Title",var.get())

r1 = Radiobutton(root,text="One",variable=var,value=1)
r1.place(x=50,y=50)

r1 = Radiobutton(root,text="Two",variable=var,value=2)
r1.place(x=50,y=100)

btn1=Button(root,text="Submit",command=display)
btn1.place(x=50,y=150)
