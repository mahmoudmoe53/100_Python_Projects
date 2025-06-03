from tkinter import *
import csv
import pandas
BACKGROUND_COLOR = "#B1DDC6"








#----------------------------------------UI-----------------------------------------------#
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

front_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_canvas.create_image(400, 263, image=front_image)
front_canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
front_canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))
front_canvas.grid(column=0, row=0, columnspan=2)


correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

correct = Button(image=correct_image, highlightthickness=0)
correct.grid(column=0, row=1)

wrong = Button(image=wrong_image, highlightthickness=0)
wrong.grid(column=1, row=1)

window.mainloop()



