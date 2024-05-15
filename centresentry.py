from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.geometry("900x800")
root.title("Centres Entry Screen")


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

name_label = Label(root, text="Name:",fg="",bg="",font=("Monotype Corsiva",40,"bold"))
pincode_label = Label(root, text="Pincode:",fg="",bg="",font=("Monotype Corsiva",40,"bold"))

name_entry = Entry(root)
pincode_entry = Entry(root)

submit_button = Button(root, text="Submit", command=submit_clicked)
clear_button = Button(root, text="Clear", command=clear_clicked)
exit_button = Button(root, text="Exit", command=exit_clicked)

name_label.place(x=50, y=100)
name_entry.place(x=200, y=100)
pincode_label.place(x=50, y=150)
pincode_entry.place(x=200, y=150)
submit_button.place(x=50, y=200)
clear_button.place(x=150, y=200)
exit_button.place(x=250, y=200)

root.mainloop()
