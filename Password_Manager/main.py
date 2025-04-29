from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

website = Entry(width=38)
website.focus()
website.grid(column=1, row=1, columnspan=2)
email = Entry(width=38)
email.insert(0, "mahmoud@gmail.com")
email.grid(column=1, row=2, columnspan=2)
password = Entry(width=21)
password.grid(column=1, row=3)

generate = Button(text="Generate Password")
generate.grid(column=2, row=3)
add = Button(text="Add", width=36)
add.grid(column=1, row=4, columnspan=2)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #




window.mainloop()