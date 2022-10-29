import pyautogui 
import time
message = 5
while message > 0:
    time.sleep(4)
    pyautogui.typewrite("This message here from python")
    time.sleep(2)
    pyautogui.press('enter')
    message = message -1
   
