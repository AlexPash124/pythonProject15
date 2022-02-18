from tkinter import *
from random import *
from tkinter import messagebox
pal = randint(20, 40)
def start():
    global pal
    palichki.config(text=pal * '|')
    comOrPlayer = randint(1, 2)
    if comOrPlayer == 1:
        compBtn['state'] = 'disabled'
    else:
        b1['state'] = 'disabled'
        b2['state'] = 'disabled'
        b3['state'] = 'disabled'

def btn1():
    global pal
    pal = pal - 1
    palichki.config(text=pal * '|')
    if pal < 1:
        messagebox.showinfo("Інфо", "Ви програли!")
    b1['state'] = 'disabled'
    b2['state'] = 'disabled'
    b3['state'] = 'disabled'
    compBtn['state'] = 'active'

def btn2():
    global pal
    pal = pal - 2
    palichki.config(text=pal * '|')
    if pal < 1:
        messagebox.showinfo("Інфо", "Ви програли!")
    b1['state'] = 'disabled'
    b2['state'] = 'disabled'
    b3['state'] = 'disabled'
    compBtn['state'] = 'active'

def btn3():
    global pal
    pal = pal - 3
    palichki.config(text=pal * '|')
    if pal < 1:
        messagebox.showinfo("Інфо", "Ви програли!")
    b1['state'] = 'disabled'
    b2['state'] = 'disabled'
    b3['state'] = 'disabled'
    compBtn['state'] = 'active'

def comRand():
    global pal
    pal = pal - randint(1, 3)
    palichki.config(text=pal * '|')
    if pal < 1:
        messagebox.showinfo("Інфо", "Комп'ютер програв!!!")
    compBtn['state'] = 'disabled'
    b1['state'] = 'active'
    b2['state'] = 'active'
    b3['state'] = 'active'

w = Tk()
w.title('Палички')
w.geometry('800x400')
w.resizable(False, False)
w.config(bg='#123')
e1Info = Label(w, text='Скільки сірників Ви хочете взяти?',
               font=('Arial', 20, 'bold'), fg='yellow', bg='#123')
e1Info.pack()
b1 = Button(w, text='1', command=btn1,
            font=('Arial', 20, 'bold'), fg='yellow', bg='#123')
b1.place(x=150, y=50)
b2 = Button(w, text='2', command=btn2,
            font=('Arial', 20, 'bold'), fg='yellow', bg='#123')
b2.place(x=300, y=50)
b3 = Button(w, text='3', command=btn3,
            font=('Arial', 20, 'bold'), fg='yellow', bg='#123')
b3.place(x=450, y=50)
palichki = Label(w, text='1',
                 font=('Arial', 40, 'bold'), fg='yellow', bg='#123')
palichki.place(x=250, y=200)
compBtn = Button(w, text="Хід Комп'ютера", command=comRand,
                 font=('Arial', 20, 'bold'), fg='yellow', bg='#123')
compBtn.place(x=300, y=300)
start()
w.mainloop()