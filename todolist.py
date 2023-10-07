import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("CodSof To-do List")

def add_task():
    task = entry.get()
    if task:
        create_checkbox(task)
        entry.delete(0, tk.END)

frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10) 

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=0, padx=5, sticky=tk.W) 

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5)

lstbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
lstbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W) 

checkboxes = []

def create_checkbox(task):
    checkbox = ttk.Checkbutton(lstbox, text=task, variable=tk.BooleanVar())
    checkboxes.append(checkbox)
    checkbox.pack()  

root.mainloop()
