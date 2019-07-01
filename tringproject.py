import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as sk

win = tk.Tk()


def m_f():
    checher = buttvar.get()
    if checher == 0:
        return 'male'
    elif checher == 1:
        return 'female'


# def check():
#     allo = curent
#     if allo == 0:
#        return 'good'
#     else:
#         return 'bad'

def get_all():
    name = user_name_entry.get()
    age = user_age_chec.get()
    gender = m_f()
    all = f'''
your name is {name} and you are {age} year old.
you are a {gender}
'''
    return all


def putter():
    bringer = get_all()
    result = ttk.Label(win, text=bringer)
    result.grid(column=1, row=6)


win.title('user profile')

user_name_promt = ttk.Label(win, text='good day please enter your name')
user_name_promt.grid(column=0, row=0)

entvar = tk.StringVar()
user_name_entry = ttk.Entry(win, textvariable=entvar)
user_name_entry.grid(column=1, row=0)

comvar = tk.StringVar()
user_age_prompt = ttk.Label(win, text='sir choose your age')
user_age_prompt.grid(column=0, row=1)
user_age_chec = ttk.Combobox(win, textvariable=comvar)
user_age_chec['value'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
user_age_chec.grid(column=1, row=1)

buttvar = tk.IntVar()
buttvar.set(20)
# male = ttk.Radiobutton(win, text='male', variable=buttvar, value='m')
# male.grid(column=0, row=2)
# female = ttk.Radiobutton(win, text='female', variable=buttvar, value='fm')
# female.grid(column=1, row=2)
gender = ['male', 'female']
for i in range(2):
    current_gen = gender[i]
    current_gen = ttk.Radiobutton(win, text=current_gen, variable=buttvar, value=i)
    current_gen.grid(column=i, row=2)

choose = ttk.Label(win, text='your best sport is: ')
choose.grid(column=0, row=3)
var = ['ball', 'tennis', 'volly ball', 'other']
for i in range(4):
    curent = i
    curent = tk.IntVar
    check = ttk.Checkbutton(win, text=var[i], variable=curent)
    check.grid(column=i + 1, row=3)

submit = ttk.Button(win, text='submit', command=putter)
submit.grid(column=1, row=4)

displayed = sk.ScrolledText(win, height=3, width=36)
displayed.grid(column=1, row=5)

win.mainloop()
