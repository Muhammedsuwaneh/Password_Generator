from tkinter import *
from random import shuffle, choices
import string
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Password Generator")
root.iconbitmap("icon.ico")
root.geometry("570x570")

# Design

# images
image1 = ImageTk.PhotoImage(Image.open('icon.ico'))

# frames
frame1 = LabelFrame(root, padx=5, pady=5)
frame1.pack(padx=20, pady=20)
frame2 = LabelFrame(root, padx=5, pady=5)
frame2.pack(padx=5, pady=5)
frame3 = LabelFrame(root, padx=5, pady=5)
frame3.pack(padx=5, pady=5)
frame4 = LabelFrame(root, padx=5, pady=5)
frame4.pack(padx=5, pady=5)

label1 = Label(frame1, text="Password Generator", font=("Verdana", 20))
label1.pack()
label2 = Label(frame1, image=image1, font=("Verdana", 5))
label2.pack()

e = Entry(frame2, font=("Verdana", 20))
e.pack()

# App Logic
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
characters = ['@', '#', '&', '$', '£', '%', '?']
lower_case_letters = list(string.ascii_lowercase)
upper_case_letters = list(string.ascii_uppercase)

password = numbers
password.extend(characters)
password.extend(lower_case_letters)
password.extend(upper_case_letters)


def generate_password():
    global password_copy
    new_password = choices(population=password, k=10)
    password_copy = new_password
    e.delete(0, END)
    e.insert(END, new_password)


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_copy)


Button(frame3, text="Copy to clipboard", font=("Verdana", 10), command=copy_to_clipboard).pack()
Button(frame4, text="Generate Password", font=("Verdana", 25), command=generate_password).pack()

root.mainloop()
