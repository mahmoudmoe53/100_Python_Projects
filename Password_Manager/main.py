from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

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
  new_data = {
    website_data: {
    "email": email_data,
    "password": password_data
  }
              }

  if len(website_data) == 0 or len(password_data) == 0:
    messagebox.showerror(title="Error", message="The Website/Password field is empty.")
  else:
    try:
      with open("data.json", "r") as f:
          data = json.load(f)

    except FileNotFoundError:
      with open("data.json", "w") as f:
        json.dump(new_data, f, indent=4)
    else:
      data.update(new_data)
      with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    finally:
      website.delete(0, END)
      password.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
  try:
    with open("data.json", "r") as i:
      passwords = json.load(i)
      websites = website.get()
  except FileNotFoundError:
    messagebox.showerror(title="Error", message="No Data File Found")
  else:
    try:
      messagebox.showinfo(title="Login Details", message=f"Email: {passwords[websites]["email"]}\n"
                                                         f"Password: {passwords[websites]["password"]}")
    except KeyError:
      messagebox.showerror(title="Error", message="No Details For The Website Exist")



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

website = Entry(width=21)
website.focus()
website.grid(column=1, row=1)
email = Entry(width=38)
email.insert(0, "mahmoud@gmail.com")
email.grid(column=1, row=2, columnspan=2)
password = Entry(width=21)
password.grid(column=1, row=3)

generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3)
add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", width=13, command=find_password)
search.grid(column=2, row=1)

window.mainloop()