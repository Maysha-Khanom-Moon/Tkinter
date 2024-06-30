"""
create checkbuttons and 2 radiobuttons

radio button:
    values for the buttons are A and B
    ticking either prints the value of the checkbutton
    ticking the radio button unchecks the checkbutton

check button:
    ticking the checkbutton prints the value of the radio button value
    
    use tkinter var for Boolean!
"""

import tkinter as tk 
from tkinter import ttk

def check_func():
    print(check_var.get())
    check_var.set(False)


# window
window = tk.Tk()
window.title('Buttons example')
window.geometry('400x120')

# buttons
# variable = radio value(which one is ticked)
# radio var type --> radio value type
radio_var = tk.StringVar(value='No one selected')

# variable = this check button is checked or not
check_var = tk.BooleanVar()

check_button = ttk.Checkbutton(
    master=window, 
    text='Check Button', 
    variable=check_var, 
    command=lambda: print(radio_var.get()) )

radio1 = ttk.Radiobutton(
    window, 
    text="Radio1", 
    value='A', 
    command=check_func, 
    variable=radio_var)

radio2 = ttk.Radiobutton(
    window, 
    text="Radio2", 
    value='B', 
    command=check_func, 
    variable=radio_var)

check_button.pack()
radio1.pack()
radio2.pack()

# run 
window.mainloop()

