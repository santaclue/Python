from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_num = [choice(numbers) for _ in range(randint(2, 4))]
    pass_sym = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = pass_sym + pass_num + pass_letters
    shuffle(password_list)
    password = "".join(password_list)
    pass_input.insert(0, password)
    copy(password)
#---------------------------SEARCH PASSWORD----------------------------------#
def find_password():
    website= web_input.get()

    try:
        with open("data.json") as data_file:
            data= json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No Data", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}.")
            copy(password)
        else:
            messagebox.showinfo(title="Error",message="No details for the website exists.")




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data,data_file,indent=4)

            else:
                data.update(new_data)
                with open("data.json","w") as data_file:
                    json.dump(data, data_file,indent=4)
            finally:
                web_input.delete(0, END)
                pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

web_lab = Label(text="Website:", bg="white")
web_lab.grid(column=0, row=1)
web_input = Entry(width=27)
web_input.place(x=100, y=197)
web_input.focus()

email_lab = Label(text="Email/Username:", bg="white")
email_lab.grid(column=0, row=2)
email_input = Entry(width=46)
email_input.place(x=100, y=218)
email_input.insert(END, "n.mahika07@gmail.com")

pass_lab = Label(text="Password:", bg="white")
pass_lab.grid(column=0, row=3)
pass_input = Entry(width=27)
pass_input.place(x=100, y=240)

pass_but = Button(text="Generate Password", bg="white", command=generate_password)
pass_but.place(x=274, y=238)

add_but = Button(text="Add", bg="white", width=40, command=save)
add_but.grid(row=4, column=1, columnspan=2)

search_but = Button(text="search",bg="white",width=14,command=find_password)
search_but.place(x=274,y=192)




window.mainloop()
