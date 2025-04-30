from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for i in range(randint(8, 10))]
  password_symbols = [choice(symbols) for i in range(randint(2, 4))]
  password_numbers = [choice(numbers) for i in range(randint(2, 4))]

  password_list = password_letters + password_symbols + password_numbers

  shuffle(password_list)

  final_password = "".join(password_list)
  pyperclip.copy(final_password)

  password.insert(0, final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  website_data = website.get()
  email_data = email.get()
  password_data = password.get()

  with open("data.txt", "a") as f:
    f.write(f"{website_data} | {email_data} | {password_data}\n")

  if len(website_data) == 0 or len(password_data) == 0:
    messagebox.showerror(title="Error", message="The Website/Password field is empty.")
  else:
    is_ok = messagebox.askokcancel(title="Saved", message=f"Are you sure these details are correct?:\n Website: {website_data}\n Email/Username: {email_data}\n Password: {password_data} ")
    if is_ok:
      website.delete(0, END)
      password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

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

generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3)
add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()