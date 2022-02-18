from time import *
from random import *
from tkinter import *

win = Tk()
win.title("math")
win.config(bg="yellow")
win.geometry("500x500")
p = 1

def chec():
    global p
    if q15.get() == str(p):
        print("you right")


def start():
    global x
    start.destroy()
    label.destroy()
    z = randint(1, 12)
    c = choice(["/", "*", "+", "-"])
    v = randint(1, 12)
    m = randint(1, 12)
    n = choice(["/", "*", "+", "-"])
    b = randint(1, 12)
    q1 = Label(win, text=z, font=("Arial", 20))
    q1.place(x=15, y=80)
    q12 = Label(win, text=c, font=("Arial", 20))
    q12.place(x=60, y=80)
    q13 = Label(win, text=v, font=("Arial", 20))
    q13.place(x=90, y=80)
    q14 = Label(win, text="=", font=("Arial", 20))
    q14.place(x=140, y=80)
    q15 = Entry(win, text="", font=("Arial", 20), width=10)
    q15.place(x=170, y=80)
    q2 = Label(win, text=b, font=("Arial", 20))
    q2.place(x=15, y=140)
    q22 = Label(win, text=n, font=("Arial", 20))
    q22.place(x=60, y=140)
    q23 = Label(win, text=b, font=("Arial", 20))
    q23.place(x=90, y=140)
    q24 = Label(win, text="=", font=("Arial", 20))
    q24.place(x=140, y=140)
    q25 = Entry(win, text="", font=("Arial", 20), width=10)
    q25.place(x=140, y=140)
    check = Button(win, text="check", font=("Arial", 20), command=chec)
    check.place(x=200, y=250)
    if c == "/":
        p = z / v
        round(p)
    elif c == "+":
        p = z + v
    elif c == "-":
        p = z - v
    elif c == "*":
        p = z * v
    while x != 0:
        sleep(1)
        x = x - 1
        time.configure(text=x)
        win.update()


x = 60
time = Label(win, text=x, font=("Arial", 20))
time.place(x=240, y=30)
label = Label(win, text="це викторина. В ній ви повинні рішити три приклади за 60 секунд", font=("Arial", 12))
label.place(x=15, y=60)
start = Button(win, text="START", font=("Arial", 20), command=start)
start.place(x=205, y=90)
win.mainloop()