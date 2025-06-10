from tkinter import *
import random
import requests


def get_quote():
    hadith_number = random.randint(2932, 3047)

    hadith_response = requests.get(f"https://hadeethenc.com/api/v1/hadeeths/one/?language=en&id={hadith_number}")

    hadith_data = hadith_response.json()

    canvas.itemconfig(quote_text, text=hadith_data["hadeeth"])




window = Tk()
window.title("Hadith Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Press button to generate hadith...", width=250, font=("Arial", 12, "bold"), fill="white")
canvas.grid(row=0, column=0)

moon_img = PhotoImage(file="moon.png")
moon_img = moon_img.subsample(10, 10)
moon_button = Button(image=moon_img, highlightthickness=0, command=get_quote)
moon_button.grid(row=1, column=0)


window.mainloop()