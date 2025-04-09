from tkinter import *

window = Tk()
window.title("Mahmoud")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


#Label
my_label = Label(text="My Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text" #This is one way of editing Kwargs
my_label.config(text="Newest Text") #This is another way
my_label.pack() #This is a way of placing your widget on a screen
my_label.place(x=0, y=0) #This is another way of placing your widget on the screen by using coordinates
my_label.grid(column=0, row=0) #This is also a way of placing a widget on a screen and probably the best way,
                               # as it is relative to your other widgets

#Button
def button_clicked():
    new_text = my_input.get()
    my_label.config(text=new_text)

my_button = Button(text="Click Here", command=button_clicked)
# my_button.pack()
my_button.grid(column=1, row=1)

#Entry
my_input = Entry(width=10)
# my_input.pack()
my_input.grid(column=3, row=2)


#new_button

new_button = Button(text="new button")
new_button.grid(column=2, row=0)

