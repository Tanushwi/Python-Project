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

name_label = Label(root, text="Name:")
pincode_label = Label(root, text="Pincode:")

name_entry = Entry(root)
pincode_entry = Entry(root)

submit_button = Button(root, text="Submit", command=submit_clicked)
clear_button = Button(root, text="Clear", command=clear_clicked)
exit_button = Button(root, text="Exit", command=exit_clicked)

name_label.place()
name_entry.place()
pincode_label.place()
pincode_entry.place()
submit_button.place()
clear_button.place()
exit_button.place()

root.mainloop()
