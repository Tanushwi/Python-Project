from tkinter import *
import time

root=Tk()
photo=PhotoImage(file="D:\Download Data\Simple.png")
l=Label(root)
l.configure(image=photo)
l.place(x=0,y=0)

root.attributes("-fullscreen",True)
root.title("INTRODUCTION")

l0=Label(root,text=" COVID-19  \n TESTING \n MANAGEMENT ")
l1=Label(root,text=" SUBMITTED BY : ")
l2=Label(root,text=" Tanushwi Singh ")
l3=Label(root,text=" Vishakha Saldi ")
l0.place(x=480,y=100)
l1.place(x=520,y=400)
l2.place(x=550,y=500)
l3.place(x=560,y=570)
def waitfn():
    time.sleep(1)
    root.destroy()


root.after(5000,waitfn)
root.mainloop()
