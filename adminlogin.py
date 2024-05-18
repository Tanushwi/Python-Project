from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.geometry("900x800")
root.title("Centres Entry Screen")
root.configure(background='lightgray')  

def submit_clicked():
    name_text = name_entry.get()
    pincode_text = pincode_entry.get()
    
    conn = sqlite3.connect("mydatabase.sqlite")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,pincode TEXT)''')

    c.execute("INSERT INTO users (name, pincode) VALUES (?, ?)", (name_text, pincode_text))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Data submitted successfully")

def clear_clicked():
    name_entry.delete(0, END)
    pincode_entry.delete(0, END)

def exit_clicked():
    root.destroy()

title_label = Label(root, text="Centres Entry Screen", font=("Monotype Corsiva", 50, "bold"), fg="navy", bg="lightgray")
title_label.place(x=200, y=50)

name_label = Label(root, text="Name:", font=("Monotype Corsiva", 30, "bold"), fg="black", bg="lightgray")
pincode_label = Label(root, text="Pincode:", font=("Monotype Corsiva", 30, "bold"), fg="black", bg="lightgray")

name_entry = Entry(root, font=("Arial", 20))
pincode_entry = Entry(root, font=("Arial", 20))

submit_button = Button(root, text="Submit", command=submit_clicked, font=("Arial", 20))
clear_button = Button(root, text="Clear", command=clear_clicked, font=("Arial", 20))
exit_button = Button(root, text="Exit", command=exit_clicked, font=("Arial", 20))

name_label.place(x=50, y=200)
name_entry.place(x=250, y=210)
pincode_label.place(x=50, y=300)
pincode_entry.place(x=250, y=310)
submit_button.place(x=200, y=400)
clear_button.place(x=350, y=400)
exit_button.place(x=500, y=400)

root.mainloop()

