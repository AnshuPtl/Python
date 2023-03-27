#write a programe to create GUI interface

from tkinter import *

root = Tk()

root.title("My Project")

root.geometry("500x500")

name = Label(root,text="Enter your name: ")
name.place(x=10,y=10)

e1=Entry(root)
e1.place(x=110,y=12.5)

btn=Button(root,text="Submit",font=("Ariel 10"),foreground="white", background="black")
btn.place(x=75,y=50)
