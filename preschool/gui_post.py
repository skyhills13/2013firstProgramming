from Tkinter import *

app = Tk()
app.title("NEXT Deliveries")
app.geometry('600x600+100+100')

def save_data():
	fileD = open("Deliveries.txt","w")
	fileD.write("Depot:\n")
	fileD.write("%s\n" %Depot.get())
	fileD.write("Description:\n")
	fileD.write("%s\n" %Description.get())
	fileD.write("Address:\n")
	fileD.write("%s\n" %Address.get("1.0",END))
	fileD.close()
	Depot.delete(0,END)
	Description.delete(0,END)
	Address.delete("1.0",END)

Label(app, text = "Depot").pack()
Depot = Entry(app)
Depot.pack()
Label(app, text = "Description").pack()
Description = Entry(app)
Description.pack()
Label(app, text = "Adress").pack()
Address=Text(app)
Address.pack()

b = Button(app, text= "save", command = save_data)
b.pack()

app.mainloop()