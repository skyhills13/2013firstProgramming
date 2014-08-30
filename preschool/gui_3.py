from Tkinter import *

app = Tk()
app.title("Entry Example")
app.geometry('300x100+100+100')

my_entry_field = Entry(app)
my_entry_field.pack()

def get_field():
	print(my_entry_field.get())
b1 = Button(app, text = 'get data', command=get_field)
b1.pack()

def insert_data():
	my_entry_field.insert(0,"hello ")
b2 = Button(app, text = 'insert', command = insert_data)
b2.pack()

def delete_field():
	my_entry_field.delete(0,END)
b3 = Button(app, text = 'delete', command = delete_field)
b3.pack()
app.mainloop()