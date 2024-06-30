import tkinter as tk
from tkinter import ttk

def button_func():
    print('button was pressed')

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk widgets
label = ttk.Label(master=window, text='This is a text', font='Calibri 20')
label.pack()

# create widgets
text = tk.Text(master=window, height=10, width=50)
text.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# ttk button
button = ttk.Button(master=window, text='A button', command=button_func)
button.pack()

# exercise
tk.Text(master=window, height=10, width=50).pack(pady=10)

ttk.Entry(master=window).pack()

ttk.Label(master=window, text="my label").pack()

ttk.Button(master=window, text='print hello', command=lambda: print('Hello')).pack()

# run
window.mainloop()