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
elif system_os == "Windows":
    file_sep = '\\'
else:
    raise Exception('system not supported')

# check Psychopy version
psychopy_info = info.RunTimeInfo()
if psychopy_info['psychopyVersion'] != "2022.2.4":
    print("The PsychoPy version is not supported, use 2022.2.4 instead")
    core.quit()

# Experiment information
expInfo = {'participant':'', 'session': ['Test', 'Experiment']}
expInfo['Date'] = data.getDateStr()

# GUI
dlg = gui.DlgFromDict(expInfo, title='fMRI course project', fixed=['Date'])
if dlg.OK == False:
    core.quit()

# Data handling
if os.path.isdir('Data') == False: # check if data file is exist, if not create one
    try:
        os.mkdir('Data')
    except:
        print('can\'t create directory, please check permission or your system specification')

fileName = expInfo['participant']+'_'+ expInfo['Date'] + expInfo['session']
exp_manager = data.ExperimentHandler(name="HRT Paradigm", version='0.1.0', extraInfo=expInfo, \
                                        dataFileName='Data'+file_sep+fileName) # this is te experiment manager for saving behaviour data and other experiment information


# counter function
TR_counter_global = 0

def scanner_counter(number): # this function is used to act like a clock to count the time by scanner inputs
    counter = 0
    while counter < number:
        keys = event.getKeys()
        if '5' in keys:
            counter += 1
            global TR_counter_global
            TR_counter_global += 1


# window initialization
win = visual.Window([1920,1080], allowGUI= True, monitor='testMonitor', units='pix', fullscr=False)

# Hide the mouse
win.mouseVisible = False

## Experiment

#Generates the Random Order of Trials for the Run as well as Jitter Lengths for each Run with an Average of 2 TRs
#0,4=sq. house; 1,5=sq. face; 2,6= ov. house; 3,7=ov. face; 4-7=oddball
trial_seq = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1,2 ,2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7]
random.shuffle(trial_seq)

trial_type_lookup = ['sq. face', 'sq. house', 'ov. face', 'ov. house', 'sq. face OB', 'sq. house OB', 'ov. face OB', 'ov. house OB']

print('Trial Sequence %s' %trial_seq)

nr_of_trials = len(trial_seq)

print('Nr. of trials: %d' %nr_of_trials)

jitter = np.asarray(range(1, nr_of_trials + 1)) % 3 + 1
np.random.shuffle(jitter)

print('Jitter lengths: %s' %(jitter+1))

# Experiment component
instruction_text = visual.TextStim(win, pos=[0,0], height=40, text="Instruction", color=[1,1,1], units='pix')

prompts =[['SFPrompt1', 'SFPrompt2'],['SHPrompt1'],['OFPrompt1','OFPrompt2'],['OHPrompt1','OHPrompt2']]
for i in range(len(prompts)):
    for j in range(len(prompts[i])):
        prompts[i][j] = visual.ImageStim(win, pos=[0,0], image='Pictures%s%s.png' %(file_sep, prompts[i][j]), units='pix')


test = visual.TextStim(win, pos=[0,0], height=40, text="jitter", color=[1,1,1], units='pix')

fixation = visual.ShapeStim(win, pos=[0,0],
                            vertices=((0, -30), (0, 30), (0,0), (-30,0), (30, 0)),
                            lineWidth=3,
                            closeShape=False,
                            lineColor="white")

stimuli = np.ndarray((2,4), dtype=object)
stimuli[0,0] = [visual.ImageStim(win, pos=[0,0], size=(400,400), image='stimulus_variations%ssquare_1.png' %(file_sep), units='pix')]
stimuli[1,0] = [visual.ImageStim(win, pos=[0,0], size=(400,400), image='stimulus_variations%soval_1.png' %(file_sep), units='pix')]
for i in range(1,4):
    _squares = []
    _ovals = []
    for j in range(6):
        _squares.append(visual.ImageStim(win, pos=[0,0], size=(400,400), image='stimulus_variations%ssquare_%d_var%d.png' %(file_sep, i+1, j+1), units='pix'))
        _ovals.append(visual.ImageStim(win, pos=[0,0], size=(400,400), image='stimulus_variations%soval_%d_var%d.png' %(file_sep, i+1, j+1), units='pix'))
    stimuli[0,i] = _squares
    stimuli[1,i] = _ovals

_stim = None

stimulus_presentation_time = 0.45

responses = [] #responses to the oddball stimuli (True = correct response)

# Instruction
instruction_text.draw()
win.flip()

# wait for the first few 5 sent by the scanner to proceed
scanner_counter(4)
exp_manager.addData('experiment.onset_tr', TR_counter_global)
t = clock.getAbsTime()
exp_manager.addData('experiment.onset',t)

for i in range(nr_of_trials):
    scanner_counter(1)
    # start of trial
    print('Trial %d on TR %d' %(i + 1, TR_counter_global))

    trial_type = trial_seq[i]
    exp_manager.addData('trial.type', trial_type_lookup[trial_type])
    exp_manager.addData('trial.start', TR_counter_global)
    oddball = -1
    if trial_type >= 4:
        oddball = random.choice(range(1,4))
    trial_type = trial_type % 4
    stimulus_type = trial_type // 2
    _variation = random.choice(range(6))

    _prompt = random.choice(prompts[trial_type])
    _prompt.draw() # prompt presentation

    fixation.draw()

    win.flip()
    
    exp_manager.addData('Prompt.onset', TR_counter_global) # maybe it makes sense to track trial onset and offset instead of prompts and stimuli, as those are only one TR in length
    t = clock.getAbsTime()
    exp_manager.addData('Prompt.onset_tr',t)
    exp_manager.addData('Prompt.file', _prompt.image)
    
    scanner_counter(1) # prompt delay
    
    
    fixation.draw()
    win.flip()
    
    scanner_counter(jitter[i]) # Jitter between Prompt and Stimulus (previous call of scanner_counter adds the additional TR needed)

    for j in range(4):  # Stimulus Presentation
        scanner_counter(1)
        ob_flag = False
        if j == oddball:
            _stim.draw()
            ob_flag = True
        else:
            if j == 0:
                _stim = stimuli[stimulus_type, j][0]
            else:
                _stim = stimuli[stimulus_type, j][_variation]

            _stim.draw()
        exp_manager.addData("Stimulus{}.img".format(j+1), _stim.image)
        fixation.draw()
        win.flip()

        core.wait(stimulus_presentation_time)
        fixation.draw()
        win.flip()

        core.wait(1.4 - stimulus_presentation_time)
        # check for response in oddball trials
        if ob_flag:
            correct_response = False

            resp = event.getKeys()

            for key in resp:
                if key == '1':
                    correct_response = True
                    print('Correct Response')
            exp_manager.addData("Response", correct_response)
            responses.append(correct_response)
    # End of trial

        exp_manager.addData("Stimulus{}".format(j+1), TR_counter_global)
    exp_manager.addData("Trial.end", TR_counter_global)
    scanner_counter(1)  # Intertrial Rest Period !! this line should stay at this indentation !!

    fixation.draw()
    win.flip()
    scanner_counter(7)
    exp_manager.nextEntry()

scanner_counter(12) # End of Run Baseline
print('End of experiment on TR %d' %TR_counter_global)
exp_manager.addData('experiment.end_TR', TR_counter_global)
t = clock.getAbsTime()
exp_manager.addData('experiment.end', t)

## Quit the Experiment
win.close()
core.quit()
