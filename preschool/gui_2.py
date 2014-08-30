from Tkinter import *

app = Tk()
app.title("Tkinter application for practice")
app.geometry('600x300+200+100')

message = StringVar()
message.set('')

def button_click():
	message.set('I have just been clicked')

l = Label(app, text = 'when you are ready, click on the button', height = 3)
l.pack()

b1 = Button(app, text = "click me", width = 10, command = button_click)#()is not needed cuz it is not the time for import right now.
#b is included in "app"(which is window now)
b1.pack(padx=10, pady=10) #w/o this command, window show nothing
# padx pady is for the invisible boundary

lm= Label(app, textvariable = message) #textvariable(0), text(x) cuz it is variable
lm.pack()

app.mainloop()