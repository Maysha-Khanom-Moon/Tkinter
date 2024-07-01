# Function with arguments button
import tkinter as tk
from tkinter import ttk

def button_func(param):
    print(f'{param} button was pressed')

# window
window = tk.Tk()
window.title('Function with arguments')
window.geometry('300x100')

# widgets
entry_string = tk.StringVar(value='test')
entry = ttk.Entry(
    master=window,
    textvariable=entry_string
)

button = ttk.Button(
    master=window,
    text='button',
    command=lambda: button_func(entry_string.get())
)

entry.pack()
button.pack()

# run
window.mainloop()