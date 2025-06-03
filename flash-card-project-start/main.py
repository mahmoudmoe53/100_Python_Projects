from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word_to_guess, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word_to_guess, text=current_card["English"], fill= "white")
    canvas.itemconfig(card_background, image=back_image)

def is_known():
    words_to_learn.remove(current_card)
    info  = pandas.DataFrame(words_to_learn)
    info.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#----------------------------------------UI-----------------------------------------------#
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=front_image)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_to_guess = canvas.create_text(400, 263, text="words", font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

correct = Button(image=correct_image, highlightthickness=0, command=is_known)
correct.grid(column=0, row=1)

wrong = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong.grid(column=1, row=1)
next_card()

window.mainloop()



