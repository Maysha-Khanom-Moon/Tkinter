"""
create 2 entry fields and 1 label, they should all be connected via StringVar
set a start value of 'test'
"""

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Example")
window.geometry('300x100')

# tk variables
string_var = tk.StringVar(value='test')

# ttk widgets
label = ttk.Label(master=window, textvariable=string_var)

entry1 = ttk.Entry(master=window, textvariable=string_var)

entry2 = ttk.Entry(master=window, textvariable=string_var)

label.pack()
entry1.pack(pady=10)
entry2.pack()

# run
window.mainloop()