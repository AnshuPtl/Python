#write a programe to create message popup in GUI interface

from tkinter import *
#import tkinter.messagebox
import tkinter.messagebox as msg

def display_data():
    if e1.get()=="":
        msg.showinfo("Alert: ","Name field is mandatory!!!")

    else:
        msg.showinfo("Your Name:",e1.get())

root=Tk()
root.title("Pop-Up")
root.geometry("700x700")

name = Label(root,text="Enter your name: ")
name.place(x=10,y=10)

e1=Entry(root)
e1.place(x=110,y=12.5)

btn=Button(root,text="Submit",font=("Ariel 10"),foreground="white", background="black", command=display_data)
btn.place(x=75,y=50)

