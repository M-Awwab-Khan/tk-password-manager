from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sv_ttk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    ws = website.get()
    em = email.get()
    pd = password.get()

    is_ok = messagebox.askokcancel(title=ws, message=f'These are the details entered: \nEmail: {em}\nPassword: {pd}\nIs it ok to save')
    if is_ok:
        with open('data.txt', 'a') as f:
            to_write = f"{ws} | {em} | {pd}\n"
            f.write(to_write)
            website.delete(0, END)
            password.delete(0, END)

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

website = ttk.Entry(width=42)
website.grid(row=1, column=1, columnspan=2, pady=5)
website.focus()
email = ttk.Entry(width=42)
email.grid(row=2, column=1, columnspan=2, pady=5)
email.insert(0, 'awwabkhan@gmail.com')
password = ttk.Entry(width=23)
password.grid(row=3, column=1, pady=5)

add = ttk.Button(text='Add', width=42, command=save_password).grid(row=4, column=1, columnspan=2, pady=5)
gen_pass = ttk.Button(text='Generate Password').grid(row=3, column=2)

sv_ttk.set_theme('light')
window.mainloop()