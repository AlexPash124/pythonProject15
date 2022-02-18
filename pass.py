from tkinter import *
from random import *


def generationPass():
    x = ''
    for i in range(int(size.get())):
        x = choice(
            ["a", "s", "d", "f", "g", "h", "j", "k", "l", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "z", "x",
             "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9"]) + x
    generPass.configure(text=x)

window = Tk()
window.title('Генератор паролів')
window.geometry('500x500')
window.resizable(False, False)
window.config(bg='#123')

size = Entry(window, text='1', font=('Arial', 30), fg='#434323')
size.place(x=30, y=50)
info = Label(window, text="Введіть кількість символів", font=('Arial', 20), fg='#434323')
info.place(x=60, y=100)
generPass = Label(window, text="", font=('Arial', 20), fg='#434323')
generPass.place(x=60, y=200)

btnGen = Button(window, command=generationPass, text='Генеруємо пароль', font=('Arial', 20), fg='#434323')
btnGen.place(x=90, y=300)
window.mainloop()
