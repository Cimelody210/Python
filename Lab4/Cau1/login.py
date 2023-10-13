from tkinter import *
parent = Tk()
parent.title('Basic login form')
parent.geometry('400x300')

name = Label(parent, text = "Name",  font='24px').grid(row = 0, column = 0)
password = Label(parent, text = "Password", font='24px').grid(row = 1, column = 0)
submit = Button(parent, text = "Submit", font='24px', padx=20).grid(row = 4, column = 0)

e1 = Entry(parent).grid(row = 0, column = 1)
e2 = Entry(parent).grid(row = 1, column = 1)
e2 = Entry(parent).grid(row = 1, column = 1)

parent.mainloop()