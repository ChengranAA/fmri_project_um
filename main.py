"""
Title:
Author:


"""

from psychopy import core, visual, gui, data, event, sound, prefs, clock,info
from psychopy.tools.filetools import fromFile, toFile
import os, csv, random, serial, platform
import numpy as np
import psychtoolbox as ptb

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
