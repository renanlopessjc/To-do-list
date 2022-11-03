from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
root.title('To-Do List')
root.geometry('300x400')
root.resizable(0, 0)
root.config(bg="Black")


new_item_entry = Entry(root, width=37)
new_item_entry.place(x=35, y=310)

add_btn = Button(root, text='Add Item', bg='Azure', width=10, font=('Helvetica', 12),

root.mainloop()
