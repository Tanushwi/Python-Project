from tkinter import *
from tkinter import messagebox
import sqlite3
import os

root=Tk()
root.geometry("900x800")
root.title("Admin Login Screen")

txtuname=StringVar()
txtpass=StringVar()

def create_clicked():
    con=sqlite3.connect("mydatabase.sqlite")
    c=con.cursor()
    u=txtuname.get()
    p=txtpass.get()
    c.execute("select * from newadminlogin where username=? ",(u,))
    datalist=c.fetchall()
    if len(datalist)>0:
        messagebox.showinfo("Alert","Username already exits..")
    else:
        c.execute("insert into newuserlogin(name,phoneno,username,password) values (?,?,?,?)",(n,ph,u,p))
        con.commit()
        messagebox.showinfo("Congrats","User Created..")
    clear_clicked()
    t1.focus()
    con.close()

def exit_clicked():
    root.destroy()

def clear_clicked():
    txtuname.set("")
    txtpass.set("")

def back_clicked():
    root.destroy()
    os.system("adminlogin.py")

l0=Label(root,text="Create User Screen")
l1=Label(root,text="Enter Username")
l2=Label(root,text="Enter Password")
t1=Entry(root,textvariable=txtuname)
t2=Entry(root,textvariable=txtpass,show="*")
l0.place(x=150,y=50)
l1.place(x=100,y=150)
l2.place(x=100,y=250)
t1.place(x=200,y=150)
t2.place(x=200,y=250)
b0=Button(root,text="Login",command=create_clicked)
b1=Button(root,text="Back",command=back_clicked)
b2=Button(root,text="Clear",command=clear_clicked)
b0.place(x=150,y=400)
b1.place(x=250,y=400)
b2.place(x=350,y=400)
t1.focus()
root.mainloop()
