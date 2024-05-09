from tkinter import *
from tkinter import messagebox
import sqlite3

def submit_record():
    patient_name = name_entry.get()
    test_result = result_var.get()

    if not patient_name or not test_result:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS patient_records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    patient_name TEXT,
                    test_result TEXT)''')

    c.execute("INSERT INTO patient_records (patient_name, test_result) VALUES (?, ?)", (patient_name, test_result))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Patient record submitted successfully")

    clear()

def clear():
    name_entry.delete(0, END)
    result_var.set("Negative")

def exit():
    root.destroy()

root = Tk()
root.geometry("400x200")
root.title("Patient Record Entry")

name_label = Label(root, text="Patient Name:")
result_label = Label(root, text="Test Result:")


name_entry = Entry(root)
result_var = StringVar(value="Negative")
result_combobox = OptionMenu(root, result_var, "Negative", "Positive")


submit_button = Button(root, text="Submit", command=submit_record)
clear_button = Button(root, text="Clear", command=clear)
exit_button = Button(root, text="Exit", command=exit)

name_label.place(x=50, y=30)
name_entry.place(x=200, y=30)
result_label.place(x=50, y=70)
result_combobox.place(x=200, y=70)
submit_button.place(x=50, y=120)
clear_button.place(x=150, y=120)
exit_button.place(x=250, y=120)

root.mainloop()
