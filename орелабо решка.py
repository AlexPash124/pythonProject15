from tkinter import *
from random import *

winner = 0
lose = 0


def Orel():
    global winner
    global lose
    comp = choice(['Орел', 'Решка'])
    if comp == 'Орел':
        result.configure(text='Перемога')
        winner = winner + 1
        win.configure(text=winner)
    else:
        result.configure(text='Поразка')
        lose += 1
        loseL.configure(text = lose)

def Reshka():
    global winner
    global lose
    comp = choice(['Орел', 'Решка'])
    if comp == 'Решка':
        result.configure(text='Перемога')
        winner = winner + 1
        win.configure(text = winner)
    else:
        result.configure(text='Поразка')
        lose += 1
        loseL.configure(text=lose)
def Clear():
    global winner
    global lose
    winner=0
    lose = 0
    #result.configure(text='0')
    win.configure(text=0)
    loseL.configure(text=0)
window = Tk()
window.title('Орел решка')
window.resizable(False, False)
window.geometry('700x700')
window.config(bg='#123')

e1 = Label(window, text="Привіт! Ти на грі Орел або решка",
           font=('Arial', 20, 'bold'), bg='#123', fg='#FFF')
e1.place(x=100, y=10)
result = Label(window, text="Результат",
               font=('Arial', 20, 'bold'), bg='#123', fg='#FFF')
result.place(x=100, y=100)

win = Label(window, text="win",
            font=('Arial', 20, 'bold'), bg='#123', fg='#FFF')
win.place(x=100, y=200)
loseL = Label(window, text="lose",
            font=('Arial', 20, 'bold'), bg='#123', fg='#FFF')
loseL.place(x=500, y=200)


orel = Button(window, command=Orel, text="Орел",
              font=('Arial', 20, 'bold'), bg='#123', fg='#FFF')
orel.place(x=100, y=420)

reshka = Button(window, command=Reshka, text="Решка",
                font=('Arial', 20, 'bold'), bg='#123', fg='#FFF')
reshka.place(x=400, y=420)

clear = Button(window, command=Clear, text="Очистити",
                font=('Arial', 20, 'bold'), bg='#123', fg='#FFF')
clear.place(x=400, y=500)
window.mainloop()
