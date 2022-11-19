"""
This program is used for testing the main experiment program.
The program simulate a fmri scanner routine by constantly sending a "5" keyboard input
"""
import time, pyautogui
tr = 1.5 # interval in ms
time.sleep(5)
print('Start scanner')

while True:
    time.sleep(tr)
    pyautogui.press('5')
