import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')


# button
def button_func(param):
    print(f'a {param} button')
    
    if check_var.get() == '1':
        print("And the checkbox ON")

button = ttk.Button(window, text='A simple button', command=lambda: button_func('Simple'))
button.pack()


# chcekbutton
# check_var = tk.BooleanVar() ---> check either True or False
check_var = tk.StringVar()

# get function does not work. to check the value, always need a variable
check = ttk.Checkbutton(window, 
    text='checkbox1', 
    command=lambda: button_func('checkbox'),
    variable=check_var)
check.pack()


# radio buttons
# radio define by value. if both have same value or default --> tkinter get confused and work on both
# although only one radio can selected at once 
radio1 = ttk.Radiobutton(window, text='Radiobutton 1', value='radio 1', command=lambda: button_func(radio1['value']))
radio2 = ttk.Radiobutton(window, text='Radiobutton 2', value='radio 2', command=lambda: button_func(radio2['value']))

radio1.pack()
radio2.pack()

# run
window.mainloop()