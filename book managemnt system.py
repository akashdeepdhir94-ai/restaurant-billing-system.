from tkinter import *
import mysql.connector

# Establish database connection
connection = mysql.connector.connect(
    host="localhost",        # MySQL server host
    user="root",             # MySQL username
    password="Am@ndeep2007"  # MySQL password
)
cursor = connection.cursor()
def get_selected_row(event):
    global selected_tuple
    index = listbox.curselection()[0]
    selected_tuple = listbox.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])

def view_command():
    listbox.delete(0, END)
    for row in database.view():
        listbox.insert(END, row)

def search_command():
    listbox.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(),
                               year_text.get(), isbn_text.get()):
        listbox.insert(END, row)

def add_command():
    database.insert(title_text.get(), author_text.get(),
                    year_text.get(), isbn_text.get())
    view_command()

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def update_command():
    database.update(selected_tuple[0], title_text.get(),
                    author_text.get(), year_text.get(), isbn_text.get())
    view_command()

window = Tk()
window.title("Book Management System")

Label(window, text="Title").grid(row=0, column=0)
Label(window, text="Author").grid(row=0, column=2)
Label(window, text="Year").grid(row=1, column=0)
Label(window, text="ISBN").grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

listbox = Listbox(window, height=6, width=35)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

listbox.configure(yscrollcommand=sb.set)
sb.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>', get_selected_row)

Button(window, text="View All", width=12, command=view_command).grid(row=2, column=3)
Button(window, text="Search", width=12, command=search_command).grid(row=3, column=3)
Button(window, text="Add", width=12, command=add_command).grid(row=4, column=3)
Button(window, text="Update", width=12, command=update_command).grid(row=5, column=3)
Button(window, text="Delete", width=12, command=delete_command).grid(row=6, column=3)
Button(window, text="Close", width=12, command=window.destroy).grid(row=7, column=3)

window.mainloop()
