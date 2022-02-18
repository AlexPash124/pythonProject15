from tkinter import *
from time import sleep
from random import *
from tkinter import messagebox
import webbrowser
def time4():
    sec = 30
def Check():
    if int(e1Ans.get()) == -13 and int(e2Ans.get()) == 130 and int(e3Ans.get()) == 14:
        messagebox.showinfo("Інфо", "Ви красавчик!!!")
    else:
        messagebox.showinfo("Інфо", "Ви НЕ Праві!!!")
        webbrowser.open('https://www.kinopoisk.ru/film/689/')


window = Tk()
window.title("Вікторина")
window.resizable(False, False)
window.geometry('700x700')
window.config(bg='#123')

e1 = Label(window, text="2 - (-4-4+5)*(-5) = ", bg='#123', fg="#FFF",
           font=('Arial', 30, 'bold'))
e1.place(x=30, y=100)
e1Ans = Entry(window, text="", bg='#123', fg="#FFF",
              font=('Arial', 30, 'bold'), width=10)
e1Ans.place(x=360, y=100)

e2 = Label(window, text="10 * (-4-4-5)*(-1) = ", bg='#123', fg="#FFF",
           font=('Arial', 30, 'bold'))
e2.place(x=30, y=200)

e2Ans = Entry(window, text="", bg='#123', fg="#FFF",
              font=('Arial', 30, 'bold'), width=10)
e2Ans.place(x=360, y=200)

e3 = Label(window, text="(-4-9+4-5)*(-1) = ", bg='#123', fg="#FFF",
           font=('Arial', 30, 'bold'))
e3.place(x=30, y=300)

e3Ans = Entry(window, text="", bg='#123', fg="#FFF",
              font=('Arial', 30, 'bold'), width=10)
e3Ans.place(x=350, y=300)

btnAns = Button(window, text="Відправити", bg='#123', fg="#FFF",
                font=('Arial', 30, 'bold'), width=10, command=Check)
btnAns.place(x=400, y=500)
window.mainloop()
