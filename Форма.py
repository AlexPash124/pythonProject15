import keyboard
import mouse
import time
isCliking = False

def set_Clicker():
    global isCliking
    if isCliking:
        isCliking = False
        print("OFF")
    else:
        isCliking = True
        print("On")
keyboard.add_hotkey('Alt+Z', set_Clicker)
while True:
    if isCliking:
        mouse.double_click(button='left')
        time.sleep(0.01)


from random import *
from tkinter import *

def NewPassword():
    size = int(numPass.get())
    password = ''
    for i in range(size):
        password = password + choice(list('QWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*'))
    labelRes.config(text=password)
window = Tk()
window.title("Генератор паролів")
window.geometry('700x700')
window.resizable(width=False, height=False)
window['bg'] = 'black'
label1 = Label(window, text='Введіть кількість символів в паролів', font=('Arial', 16, 'bold'), bg='white')
label1.place(x=30, y=20)
numPass = Entry(window, text='0', font=('Arial', 16, 'bold'), width=10)
numPass.place(x=30, y=70)
labelRes = Label(window, text='Згенерований пароль', font=('Arial', 16, 'bold'), bg='white')
labelRes.place(x=30, y=150)
Start = Button(window, command=NewPassword, text='Start', font=('Arial', 16, 'bold'), width=10)
Start.place(x=250, y=250)
window.mainloop()