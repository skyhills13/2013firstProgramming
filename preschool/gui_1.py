from Tkinter import *

app = Tk()
app.title("Tkinter application for practice")
app.geometry('600x300+200+100')

def button_click():
	print("I have just been clicked")

l = Label(app, text = 'when you are ready, click on the button', height = 3)
l.pack()

b1 = Button(app, text = "Top", width = 10, command = button_click)#()is not needed cuz it is not the time for import right now.
#b is included in "app"(which is window now)
b1.pack(padx=10, pady=10) #w/o this command, window show nothing
# padx pady is for the invisible boundary
b2 = Button(app, text = "Left", width = 10)
b2.pack(side='left')
b3 = Button(app, text = "Right", width = 10)
b3.pack(side='right')
b4 = Button(app, text = "Botton", width = 10)
b4.pack(side= 'bottom')
app.mainloop() # if it's not for it, the window just show up and disappear