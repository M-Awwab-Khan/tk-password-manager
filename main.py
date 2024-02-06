from tkinter import *
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

Label(text='Website: ').grid(row=1, column=0)
Label(text='Email/Username: ').grid(row=2, column=0)
Label(text='Password: ').grid(row=3, column=0)

website = Entry(width=35).grid(row=1, column=1, columnspan=2)
email = Entry(width=35).grid(row=2, column=1, columnspan=2)
password = Entry(width=21).grid(row=3, column=1)

add = Button(text='Add', width=36).grid(row=4, column=1, columnspan=2)
gen_pass = Button(text='Generate Password').grid(row=3, column=2)

window.mainloop()