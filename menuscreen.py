from tkinter import *
import os

def centresentryscreen():
    os.system("centresentry.py")
    
def deletecentrescreen():
    os.system("deletecentre.py")

def updatecentrescreen():
    os.system("updatecentre.py")
    
def patientrecordscreen():
    os.system("patientrecord.py")
    
def adminloginscreen():
    os.system("adminlogin.py")

def userloginscreen():
    os.system("userlogin.py")

def userregistrationscreen():
    os.system("userregistration.py")

root1=Tk()
photo=PhotoImage(file="C:\\Users\\DELL\\Pictures\\3-d.png")
l=Label(root1)
l.configure(image=photo)
l.place(x=0,y=0)   
root1.attributes("-fullscreen",True)
root1.title("MAIN MENU")


l0=Label(root1,text=" WELCOME \n TO \n COVID-19 \n TESTING \n MANAGEMENT ",fg="purple",font=("Monotype Corsiva",65,"bold","underline"))
l0.place(x=700,y=150)


mymenu=Menu(root1)
root1.config(menu=mymenu)


centremenu=Menu(mymenu)
loginmenu=Menu(mymenu)
registrationmenu=Menu(mymenu)
exitmenu=Menu(mymenu)

mymenu.add_cascade(label="CENTRE",font=("Britannic Bold",20,"bold"),menu=centremenu)
mymenu.add_cascade(label="LOGIN",font=("Britannic Bold",20,"bold"),menu=loginmenu)
mymenu.add_cascade(label="REGISTRATION",font=("Britannic Bold",20,"bold"),menu=registrationmenu)
mymenu.add_cascade(label="EXIT",font=("Britannic Bold",20,"bold"),menu=exitmenu)

centremenu.add_command(label="ADD CENTRE",font=("Britannic Bold",10,"bold"),command=centresentryscreen)
centremenu.add_separator()
centremenu.add_command(label="UPDATE CENTRE",font=("Britannic Bold",10,"bold"),command=updatecentrescreen)
centremenu.add_separator()
centremenu.add_command(label="DELETE CENTRE",font=("Britannic Bold",10,"bold"),command=deletecentrescreen)

loginmenu.add_command(label="ADMIN LOGIN",font=("Britannic Bold",10,"bold"),command=adminloginscreen)
loginmenu.add_separator()
loginmenu.add_command(label="USER LOGIN",font=("Britannic Bold",10,"bold"),command=userloginscreen)

registrationmenu.add_command(label="REGISTRATION",font=("Britannic Bold",10,"bold"),command=userregistrationscreen)

exitmenu.add_command(label="QUIT APP",font=("Britannic Bold",10,"bold"),command=root1.destroy)

mainloop()
