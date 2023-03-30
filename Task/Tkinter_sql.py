from tkinter import *
import tkinter.messagebox as msg
import mysql.connector

root=Tk()
root.geometry("500x500")
root.title("Tkinter")
root.resizable(False,False)
var=StringVar()

#creation of connection object

def conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tkinter_form"
        )

#--------------------Insertion of data in data table--------------------
def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or var.get()=="" or e_email.get()=="" or e_pswd.get()=="" or e_contact.get()=="" or e_address.get()=="":
        msg.showinfo("Alert","All fields are Mandatory!!!")
    else:
        connect=conn()
        cursor=connect.cursor()
        query="insert into user(FirstName,LastName,Gender,Email,Contact,Address,Password) values(%s,%s,%s,%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),var.get(),e_email.get(),e_contact.get(),e_address.get(),e_pswd.get())
        cursor.execute(query,args)
        connect.commit()
        connect.close()

        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_contact.delete(0,'end')
        e_address.delete(0,'end')
        e_pswd.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Successfully")

#--------------------Fetch data from table--------------------
def search_data():
    if e_email.get()=="":
        msg.showinfo("Alert","Email is mandatory!!!")
    else:
        connect=conn()
        cursor=connect.cursor()
        query="select * from user where Email=%s"
        args=(e_email.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()

        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_contact.insert(0,i[5])
                e_address.insert(0,i[6])
                e_pswd.insert(0,i[7])

        connect.commit()
        connect.close()

        
#--------------------Updation of data on data table--------------------
def update_data():
    if e_fname.get()==""or e_lname.get()=="" or var.get()=="" or e_email.get()=="" or e_pswd.get()=="" or e_contact.get()=="" or e_address.get()=="":
        msg.showinfo("Alert","All fields are mandatory!!!")

    else:
        connect=conn()
        cursor=connect.cursor()
        query="update user set FirstName=%s,LastName=%s,Gender=%s,Contact=%s,Address=%s,Password=%s where Email=%s"
        args=(e_fname.get(),e_lname.get(),var.get(),e_contact.get(),e_address.get(),e_pswd.get(),e_email.get())
        cursor.execute(query,args)
        connect.commit()
        connect.close()

        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_contact.delete(0,'end')
        e_address.delete(0,'end')
        e_pswd.delete(0,'end')
        msg.showinfo("Update Status","Data updated successfully")

#--------------------Deletion of data from data table--------------------

def delete_data():
    if e_email.get()=="":
        msg.showinfo("Alert","Email is mandatory!!!")
    else:
        connect=conn()
        cursor=connect.cursor()
        query="delete from user where Email=%s"
        args=(e_email.get(),)
        cursor.execute(query,args)
        connect.commit()
        connect.close()

        e_fname.delete(0,'end')
        e_lname.delete(0,"end")
        e_email.delete(0,'end')
        e_contact.delete(0,"end")
        e_address.delete(0,'end')
        e_pswd.delete(0,"end")
        msg.showinfo("Delete Status","Data deleted successfully")
        
#-----------------------LABELS--------------------
tag=Label(root,text="FORM" ,font=('Arial 16'))
tag.place(x=100,y=10)

fname=Label(root,text="First Name : " ,font=('Arial 16'))
fname.place(x=16,y=50)

lname=Label(root,text="Last Name : " ,font=('Arial 16'))
lname.place(x=16,y=90)

gender=Label(root,text="Gender : " ,font=('Arial 16'))
gender.place(x=16,y=130)

email=Label(root,text="Email Id : " ,font=('Arial 16'))
email.place(x=16,y=170)

contact=Label(root,text="Contact No : " ,font=('Arial 16'))
contact.place(x=16,y=210)

address=Label(root,text="Address : " ,font=('Arial 16'))
address.place(x=16,y=250)

pswd=Label(root,text="Password : " ,font=('Arial 16'))
pswd.place(x=16,y=290)

#--------------INPUTS--------------------

e_fname=Entry(root)
e_fname.place(x=150,y=60)

e_lname=Entry(root)
e_lname.place(x=150,y=100)

e_gender=Radiobutton (root,text="male",variable=var,value="male")
e_gender.place(x=150,y=140)

e_gender=Radiobutton (root,text="female",variable=var,value="female")
e_gender.place(x=200,y=140)

e_email=Entry(root)
e_email.place(x=150,y=180)

e_contact=Entry(root)
e_contact.place(x=150,y=220)

e_address=Entry(root)
e_address.place(x=150,y=260)

e_pswd=Entry(root)
e_pswd.place(x=150,y=300)

#--------------Button--------------------

submit=Button(root,text="SUBMIT", foreground="black", background="teal", font=('Arial 16'),command=insert_data)
submit.place(x=25,y=350)

search=Button(root,text="SEARCH", foreground="black", background="teal", font=('Arial 16'),command=search_data)
search.place(x=125,y=350)

update=Button(root,text="UPDATE", foreground="black", background="teal", font=('Arial 16'),command=update_data)
update.place(x=233,y=350)

delete=Button(root,text="DELETE", foreground="black", background="teal", font=('Arial 16'),command=delete_data)
delete.place(x=338,y=350)
