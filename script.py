import pyautogui

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