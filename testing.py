import tkinter as tk
from tkinter import ttk

win = tk.Tk()


# function or command of all our button


def colour_changer():
    get_name = first_entry.get()
    first_but.configure(text='clicked', state='disable')
    win.configure(bg='white')
    first_label.configure(text='button has ben clicked')
    ttk.Label(text='hello ' + get_name).pack()


def color_changer2():
    get_name = sec_entry.get()
    sec_but.configure(text='benn clicked too', fg='yellow', bg='green')
    win.configure(bg='yellow')
    sec_label.configure(text='sec but has been clicked too', fg='yellow', bg='green')
    tk.Label(text='hello ' + get_name, fg='yellow', bg='green').pack()


win.title('justin tring all')

# first style of label
first_label = ttk.Label(win, text='hello')
first_label.pack()
# seond style of label
sec_label = tk.Label(win, text='you are welcome', bg='blue')
sec_label.pack()

# first button
first_but = ttk.Button(win, text='click me', command=colour_changer)
first_but.pack()
# second button style
sec_but = tk.Button(win, text='click me to', command=color_changer2)
sec_but.pack()

# first entry field
first_entry_var = tk.StringVar()
first_entry = ttk.Entry(win, textvariable=first_entry_var)
first_entry.pack()
# sec entry style
sec_entry_var = tk.StringVar()
sec_entry = tk.Entry(win, textvariable=sec_entry_var, bg='black', fg='yellow')
sec_entry.pack()

win.mainloop()
