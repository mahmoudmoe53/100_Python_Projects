from tkinter import *

CALC = 1.609

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=100)

miles_input = Entry()
miles_input.insert(END, string="0")
miles_input.grid(column=0, row=0)




label = Label(text="0 miles", width=10)
label.grid(column=0, row=1)
label.config(padx=300)

def conversion():
    miles = int(miles_input.get())
    km = CALC * miles
    return label.config(text=f"{miles} miles is equivalent to {km}km")


button = Button(text="Calculate", command=conversion)
button.grid(column=0, row=2)


window.mainloop()