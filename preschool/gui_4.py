from Tkinter import *
app=Tk()
app.title("Text Example")
app.geometry('400x500+100+100')

my_text_field = Text(app) 
my_text_field.pack()

def get_data():
	print(my_text_field.get("1.0",END))
def insert_data():
	my_text_field.insert("1.0","some text")
def delete_data():
	my_text_field.delete("1.0",END)

Button(app, text = "Get data", command = get_data).pack()
Button(app, text = "insert data", command= insert_data).pack()
Button(app, text = "Delete data", command = delete_data).pack()

app.mainloop()