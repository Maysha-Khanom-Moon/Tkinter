'''
Events binding
    Widget.bind(event, function)
    
event format: 
    <modifier-type-key> # modifier + key
    or
    <type-key>

==> type will be uppercase
'''

import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

# window
window = tk.Tk()
window.title('Events binding')
window.geometry('800x500')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text='A Button')
button.pack()

# events
window.bind('<Alt-KeyPress-a>', lambda event: print('an keypress event')) # Alt + a

entry.bind('<KeyPress-Return>', lambda event: print('Enter key pressed at entry')) # Enter --> entry

button.bind('<KeyPress>', lambda event: print('any key pressed at button'))

text.bind('<Motion>', get_pos)

entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

# run
window.mainloop()