import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry
    entry_text = entry.get()
    
    # update the label
    # label.configure(text='some other text')
    label['text'] ='welcome, ' + entry_text
    entry['state'] = 'disable'
    button.pack_forget()
    back_button.pack()

def back_func():
    label['text'] = 'some text'
    entry['state'] = 'enable'
    button.pack()
    back_button.pack_forget()

# window
window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('300x100')

# widgets
label = ttk.Label(master=window, text='Some text')

entry = ttk.Entry(master=window)

button = ttk.Button(master=window, text='The button', command=button_func)

back_button = ttk.Button(master=window, text='Back button', command=back_func)

label.pack()
entry.pack()
button.pack()

# run
window.mainloop()