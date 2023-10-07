import tkinter as tk
from tkinter import ttk
import random
import string

root = tk.Tk()
root.title("Password Generator")


def generate_password():
    selected_options = [option.get() for option in checkboxes]
    password_characters = ""

    if "alphabets" in selected_options:
        password_characters += string.ascii_letters
    if "numbers" in selected_options:
        password_characters += string.digits
    if "special characters" in selected_options:
        password_characters += "!@#$%^&*()_+-=/"

    password_length = int(length_entry.get())

    if password_characters and password_length > 0:
        password_text = "".join(random.choice(password_characters) for _ in range(password_length))
        password_label.config(text="Generated Password: " + password_text)
    else:
        password_label.config(text="Please select at least one option and enter a valid length")

frame = tk.Frame(root)
frame.pack(pady=10)

options = ["alphabets", "numbers", "special characters"]
checkboxes = []

for i in options:
    var = tk.StringVar()
    checkbox = ttk.Checkbutton(frame, text=i, variable=var, onvalue=i, offvalue="")
    checkboxes.append(var)
    checkbox.pack()


length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root, width=5)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()