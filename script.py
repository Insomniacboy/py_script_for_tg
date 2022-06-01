import pyautogui
from pynput import mouse

def send():
    button7location = pyautogui.locateCenterOnScreen('unknown.png')
    pyautogui.move(button7location)

def on_click(x, y, button, pressed):
    if pressed:
        send()

# Collect events until released
with mouse.Listener(
        on_click=on_click,) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_click=on_click,)
listener.start()

"""
flag = True
file = open("results.txt", "w")
while(flag):
    val = input("Press any button once mouse is fixed or Q to terminate process... ")
    if (val!='Q'):
        currentMouseX, currentMouseY = pyautogui.position()
        file.write("currentMouseX = " + str(currentMouseX) + "; " +"currentMouseY = "+ str(currentMouseY) + "\n")
    else:
        file.close()
        break
"""
