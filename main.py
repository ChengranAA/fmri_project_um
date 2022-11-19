"""
Title:
Author:


"""

from psychopy import core, visual, gui, data, event, sound, prefs, clock, info
from psychopy.tools.filetools import fromFile, toFile
import os, csv, random, serial, platform
import numpy as np
import psychtoolbox as ptb

## Pre experiment setup
# global shut down key
event.globalKeys.add(key='escape', func=core.quit, name='shutdown')

# check system information
if platform.system() == "Darwin":
    print("You are running: MacOS")
else:
    print("You are running: ", platform.system())

system_os = platform.system()
if system_os == "Linux" or system_os == "Darwin":
    file_sep = '/'
elif os == "Windows":
    file_sep = '\\'
else:
    print("ERROR: system not support")

# check Psychopy version
psychopy_info = info.RunTimeInfo()
if psychopy_info['psychopyVersion'] != "2022.2.4":
    print("The PsychoPy version is not supported, use 2022.2.4 instead")
    core.quit()

# GUI
mydlg = gui.Dlg(title="fMRI course project")
mydlg.addField('Participant:')
mydlg.addField('Session:', choices=["Test", "Experiment"])
ok_data = mydlg.show()
if mydlg.OK == False:
    core.quit()

# counter function
def scanner_counter(number): # this function is used to act like a clock to count the time by scanner inputs
    counter = 0
    while counter < number:
        keys = event.getKeys()
        if '5' in keys:
            counter += 1


# window initialization
win = visual.Window([1920,1080], allowGUI= True, monitor='testMonitor', units='pix', fullscr=False)

## Experiment

# Experiment component
instruction_text = visual.TextStim(win, pos=[0,0], height=40, text="Instruction", color=[1,1,1], units='pix')
prompt = visual.TextStim(win, pos=[0,0], height=40, text="prompt", color=[1,1,1], units='pix')
stimuli_1 = visual.TextStim(win, pos=[0,0], height=40, text="stimuli_1", color=[1,1,1], units='pix')
stimuli_2 = visual.TextStim(win, pos=[0,0], height=40, text="stimuli_2", color=[1,1,1], units='pix')
stimuli_3 = visual.TextStim(win, pos=[0,0], height=40, text="stimuli_3", color=[1,1,1], units='pix')
stimuli_4 = visual.TextStim(win, pos=[0,0], height=40, text="stimuli_4", color=[1,1,1], units='pix')



# Instruction
instruction_text.draw()
win.flip()

# wait for the first few 5 sent by the scanner to proceed
scanner_counter(10)

# single routine
prompt.draw()
win.flip()
scanner_counter(1)
win.flip()
scanner_counter(2)
stimuli_1.draw()
win.flip()
scanner_counter(1)

stimuli_2.draw()
win.flip()
scanner_counter(1)

stimuli_3.draw()
win.flip()
scanner_counter(1)

stimuli_4.draw()
win.flip()
scanner_counter(1)


## Quit the Experiment
win.close()
core.quit()
