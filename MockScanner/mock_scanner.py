"""
This program is used for testing the main experiment program.
The program simulate a fmri scanner routine by constantly sending a "5" keyboard input
"""
import time, pyautogui,os
tr = 1.5 # interval in ms

# create a log file for the scanner
if not os.path.isfile('scanner_log.txt'):
    f = open('scanner_log.txt', 'x')

# delay
time.sleep(5)

# start scanner
print('Start scanner')
with open('scanner_log.txt', 'w') as f:
    f.write('Scanner strat\n') # create log file if there is none, and overwrite the log file

# counter initialise
counter = 0

# main loop
while True:
    time.sleep(tr)
    pyautogui.press('5')
    counter += 1
    t = time.time()
    with open('scanner_log.txt', 'a') as f:
        f.write("{}, {}\n".format(counter, t))
