'''
print 'Mousewheel' when the user holds down shift and uses the mousewhell while text is selected
'''

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Mouse Whell event')
window.geometry('800x500')

# widgets
text = tk.Text(window)
text.pack()

default_text = "Explanation: Creating the Text Widget: text = tk.Text(window, height=5, width=40) creates the Text widget with specified height and width. Inserting Default Text: text.insert('1.0', default_text) inserts the default text at the beginning of the Text widget. The index '1.0' means the first line, first character. Other Widgets and Events: The rest of the code creates the Entry widget, a Button, and binds events as before. This will display the Text widget with the specified default text when the window opens. Explanation: Creating the Text Widget: text = tk.Text(window, height=5, width=40) creates the Text widget with specified height and width. Inserting Default Text: text.insert('1.0', default_text) inserts the default text at the beginning of the Text widget. The index '1.0' means the first line, first character. Other Widgets and Events: The rest of the code creates the Entry widget, a Button, and binds events as before. This will display the Text widget with the specified default text when the window opens."
text.insert('1.0', default_text)

# events
text.bind('<MouseWheel>', lambda event: print(event))

# run
window.mainloop()