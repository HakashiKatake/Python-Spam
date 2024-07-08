
import pyautogui
import time

x = 1
y = 10
z = y + 1

while x < z:
    x = x + 0.5
    time.sleep(0.3)
    pyautogui.typewrite('yo')
    pyautogui.press('enter')
    time.sleep(0.3)

    




