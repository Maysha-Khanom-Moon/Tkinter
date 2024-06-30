
import tkinter as tk
from tkinter import ttk
'''
Entry ---> StringVar ---> Label (all done automatically)
'''

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

# window
window = tk.Tk()
window.title('Variables')
window.geometry('250x100')

# tkinter variable
string_var = tk.StringVar(value = 'start value')

# widgets
label = ttk.Label(master=window, text='label', textvariable=string_var)

entry = ttk.Entry(master=window, textvariable=string_var)

entry2 = ttk.Entry(master=window, textvariable=string_var)

button = ttk.Button(master=window, text='button', command=button_func)

label.pack()
entry.pack()
entry2.pack()
button.pack()

# run
window.mainloop()