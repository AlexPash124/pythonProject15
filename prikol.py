from tkinter import *
import webbrowser
from tkinter import messagebox
def login1():
    if login.get() == "login" and password.get() == "11111":
        e1.configure(text="Ти красава!!!")
    else:
        while(True):
            messagebox.showerror(text ="Привіт! от моє ДЗ")


window = Tk()
window.title("ДЗ")
window.geometry('500x500')
window.resizable(False, False)
window.config(bg='#123')

e1 = Label(window, text="Добрий день. Це я здаю ДЗ",
           font=('Arial', 20, 'bold'), bg='#123', fg='#FFFFFF')
e1.place(x=0, y=0)

log = Label(window, text="Login", font=('Arial', 20, 'bold'),
            bg='#123', fg='#FFFFFF')
log.place(x=0, y=100)
login = Entry(window, text='', font=('Arial', 20, 'bold'),
              bg='#123', fg='#FFFFFF')
login.place(x=0, y=150)

pas = Label(window, text="Password",
            font=('Arial', 20, 'bold'), bg='#123', fg='#FFFFFF')
pas.place(x=0, y=200)

password = Entry(window, text='', font=('Arial', 20, 'bold'),
                 bg='#123', fg='#FFFFFF')
password.place(x=0, y=250)

btn = Button(window, command=login1, text="Перевірити", font=('Arial', 20, 'bold'),
             bg='#123', fg='#FFFFFF')
btn.place(x=0, y= 400)
window.mainloop()
