"""
A program this contains books information:
Title, Author, Year, ISBN

A user can:
view all records
search any entry
add entry
delete entry

close by sachin raj  222222


from tkinter import *
import tkinter.messagebox
import backend

window = Tk()
def get_selected_row(event):
    global get_seletected_tuple
    index = list1.curselection()
    get_seletected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, get_seletected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, get_seletected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, get_seletected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, get_seletected_tuple[4])
def update_command():
    backend.update(get_seletected_tuple[0], title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())

def delete_command():
    backend.delete(get_seletected_tuple[0])


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)
def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()):
        list1.insert(END, row)
def add_entry_command():
    if title_text.get() == "" or author_text.get() == "" or year_text.get() == "" or ISBN_text.get() =="":

        tkinter.messagebox.showerror("showerror", "Error")
        #window.mainloop()

    else:
        backend.insert(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
        list1.delete(0, END)
        list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()))


#window = Tk()
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
l2 = Label(window, text="Author")
l2.grid(row=0, column=2)
l3 = Label(window, text="Year")
l3.grid(row=1, column=0)
l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)
author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)
year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)
ISBN_text = StringVar()
e4 = Entry(window, textvariable=ISBN_text)
e4.grid(row=1, column=3)
list1 = Listbox(window, height= 10, width=20)
list1.grid(row=2, column=1,rowspan=6, columnspan=2, sticky=SW)
list1.bind('<<ListboxSelect>>', get_selected_row)
scrb = Scrollbar(window)
scrb.grid(row=2, column = 2, rowspan=6)
list1.configure(yscrollcommand=scrb.set)
scrb.configure(command=list1.yview)
b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)
b2 = Button(window, text="Search", width=12, command=search_command)
b2.grid(row=3, column=3)
b3 = Button(window, text="Add entry", width=12, command=add_entry_command)
b3.grid(row=4, column=3)
b4 = Button(window, text="Update", width=12, command = update_command)
b4.grid(row=5, column=3)
b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)
b6 = Button(window, text="Close", width=12, command=window.destroy())
b6.grid(row=7, column=3)
window.mainloop()

