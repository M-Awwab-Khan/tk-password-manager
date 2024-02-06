from tkinter import *
from tkinter import ttk
import sv_ttk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

ttk.Label(text='Website: ').grid(row=1, column=0)
ttk.Label(text='Email/Username: ').grid(row=2, column=0)
ttk.Label(text='Password: ').grid(row=3, column=0)

website = ttk.Entry(width=42).grid(row=1, column=1, columnspan=2)
email = ttk.Entry(width=42).grid(row=2, column=1, columnspan=2)
password = ttk.Entry(width=23).grid(row=3, column=1)

add = ttk.Button(text='Add', width=42).grid(row=4, column=1, columnspan=2)
gen_pass = ttk.Button(text='Generate Password').grid(row=3, column=2)

sv_ttk.set_theme('light')
window.mainloop()