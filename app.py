from tkinter import *
from random import shuffle
import string
from PIL import ImageTk, Image

root = Tk()
root.title("Password Generator")
root.iconbitmap("icon.ico")
root.geometry("600x530")

# App Logic
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
characters = ['@', '#', '&', '$', '£', '%', '?']
lower_case_letters = list(string.ascii_lowercase)
upper_case_letters = list(string.ascii_uppercase)

def generate_password():
    pass

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

label1 = Label(frame1, text="Password Generator", font=("Verdana", 25))
label1.pack()
label2 = Label(frame1, image=image1, font=("Verdana", 5))
label2.pack()

entry = Entry(frame2, font=("Verdana", 20)).pack()

generate = Button(frame3, text="Generate Password", font=("Verdana", 25), command=generate_password).pack()

root.mainloop()
