from tkinter import *
from tkinter import messagebox
import sqlite3

def delete_record():
    record_id = record_id_entry.get()
    if not record_id:
        messagebox.showerror("Error", "Please enter a record ID to delete")
        return

    conn = sqlite3.connect("mydatabase.sqlite")
    c = conn.cursor()

    c.execute("select * from users WHERE id=?", (record_id,))
    record = c.fetchone()
    if not record:
        messagebox.showerror("Error", f"No record found with ID {record_id}")
        return

    confirmation = messagebox.askyesno("Confirmation", f"Do you want to delete record with ID {record_id}?")
    if confirmation:
        
        c.execute("DELETE FROM users WHERE id=?", (record_id,))
        conn.commit()
        messagebox.showinfo("Success", f"Record with ID {record_id} deleted successfully")

    conn.close()
    clear()

def clear():
    record_id_entry.delete(0, END)

def exit_app():
    root.destroy()

root = Tk()
root.geometry("900x800")
root.title("Delete Centre Screen")

record_id_label = Label(root, text="Enter Record ID:",fg="black",bg="orange",font=("Monotype",40,"bold"))
record_id_label.place(x=50, y=60)

record_id_entry = Entry(root)
record_id_entry.place(x=200, y=60)

delete_button = Button(root, text="Delete", command=delete_record)
delete_button.place(x=50, y=100)

clear_button = Button(root, text="Clear", command=clear)
clear_button.place(x=150, y=100)

exit_button = Button(root, text="Exit", command=exit_app)
exit_button.place(x=250, y=100)

root.mainloop()
