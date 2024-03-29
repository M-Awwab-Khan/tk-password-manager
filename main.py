from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sv_ttk
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    generated_password = ''.join(password_list)

    password.delete(0, END)
    password.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    ws = website.get()
    em = email.get()
    pd = password.get()
    if ws and em and pd:
        is_ok = messagebox.askokcancel(title=ws, message=f'These are the details entered: \nEmail: {em}\nPassword: {pd}\nIs it ok to save? ')
        if is_ok:
            new_entry = {
                 ws: {
                      "email": em,
                      "password": pd
                 }
            }
            try:
                with open('data.json', 'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open('data.json', 'w') as f:
                    json.dump(new_entry, f, indent=4)
            else:
                data.update(new_entry)
                with open('data.json', 'w') as f:
                    json.dump(data, f, indent=4)
            finally:
                website.delete(0, END)
                password.delete(0, END)
    else:
        messagebox.showwarning(title='Error', message="Please don't leave any fields empty!")

def search_password():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title='File Error', message='Data file not found.')
    else:
        ws = website.get()
        if ws:
            if ws in data:
                messagebox.showinfo(title='Found Entry', message=f"Email: {data[ws]['email']}\nPassword: {data[ws]['password']}")
            else:
                messagebox.showinfo(title='Not Found', message=f"Sorry! No entry exists for {ws}")
        else:
            messagebox.showerror(title='Empty Field', message='Please fill in Website field to search for')
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

ttk.Label(text='Website: ').grid(row=1, column=0, pady=5)
ttk.Label(text='Email/Username: ').grid(row=2, column=0, pady=5)
ttk.Label(text='Password: ').grid(row=3, column=0, pady=5)

website = ttk.Entry(width=23)
website.grid(row=1, column=1, pady=5)
website.focus()
email = ttk.Entry(width=42)
email.grid(row=2, column=1, columnspan=2, pady=5)
email.insert(0, 'awwabkhan@gmail.com')
password = ttk.Entry(width=23)
password.grid(row=3, column=1, pady=5)

add = ttk.Button(text='Add', width=42, command=save_password).grid(row=4, column=1, columnspan=2, pady=5)
gen_pass = ttk.Button(text='Generate Password', command=generate_password).grid(row=3, column=2)
search_pass = ttk.Button(text='Search', command=search_password, width=15).grid(row=1, column=2)

sv_ttk.set_theme('light')
window.mainloop()