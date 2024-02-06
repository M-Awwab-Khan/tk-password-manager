from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.pack()

window.mainloop()