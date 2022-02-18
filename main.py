
from tkinter import *
from random import *
from tkinter import messagebox

def Yes():
    btnYes.place(x=randint(0, 600), y=randint(0, 500))
    btnYes.place(x=randint(0, 600), y=randint(0, 500))

def no():
    btnno.place(x=randint(0, 600), y=randint(0, 500))
    btnYes.place(x=randint(0, 600), y=randint(0, 500))

window = Tk()
window.geometry('600x600')
window.title('Опитування')
window.resizable(width=False, height=False)
window['bg'] = 'black'
label = Label(window, text='Ти хочеш збільшити свою зарплату?', font='Arial 20 bold', bg='white')
label.place(x=10, y=10)
btnYes = Button(window, command=Yes, text='Так', font='Arial 20 bold', bg='white')
btnYes.place(x=100, y=300)
btnno = Button(window, text='Ні', command = no, font='Arial 20 bold', bg='white')
btnno.place(x=300, y=300)
window.mainloop()
