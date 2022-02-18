import keyboard
import mouse
import time
isClick = False
def set_Click():
    global isClick
    if isClick:
        isClick = False
        print("Off")
    else:
        isClick = True
        print("On")
keyboard.add_hotkey('Alt+z', set_Click)
while True:
    if isClick:
        mouse.double_click(button='left')
        time.sleep(0.01)
