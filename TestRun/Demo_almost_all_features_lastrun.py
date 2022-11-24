#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on November 24, 2022, at 15:08
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
scanner_msg = "Waiting for Scanner"
counter = 1
counter_list = []
# Run 'Before Experiment' code from code_4
condition = ""


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'Demo_almost_all_features'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\herrd\\Documents\\GitHub\\fmri_project_um\\TestRun\\Demo_almost_all_features_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "routine_5TR_PrePeriod" ---
waiting_TR = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='Waiting for Scanner',
    font='Open Sans',
    pos=(0, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
# Run 'Begin Experiment' code from code
filename2 = "test"
thisExp2 = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\herrd\\Documents\\GitHub\\fmri_project_um\\TestRun\\Demo_almost_all_features.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename2)

fixation_cross = visual.ShapeStim(
    win=win, name='fixation_cross', vertices='cross',
    size=(0.025, 0.025),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)

# --- Initialize components for Routine "Prompt" ---
text_9 = visual.TextStim(win=win, name='text_9',
    text='',
    font='Open Sans',
    pos=(0,0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Prompts = visual.ImageStim(
    win=win,
    name='Prompts', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Prompt1TR = keyboard.Keyboard()
fixation_cross_8 = visual.ShapeStim(
    win=win, name='fixation_cross_8', vertices='cross',
    size=(0.025, 0.025),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "RestEither3or6Secs" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='',
    font='Open Sans',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()
fixation_cross_2 = visual.ShapeStim(
    win=win, name='fixation_cross_2', vertices='cross',
    size=(0.025, 0.025),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "Stimulus1" ---
StimuliTimer1 = visual.TextStim(win=win, name='StimuliTimer1',
    text='',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Stimuli1 = visual.ImageStim(
    win=win,
    name='Stimuli1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
TR_Stim1 = keyboard.Keyboard()
oddball1 = keyboard.Keyboard()
fixation_cross_3 = visual.ShapeStim(
    win=win, name='fixation_cross_3', vertices='cross',
    size=(0.025, 0.025),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "Stimulus2" ---
StimuliTimer2 = visual.TextStim(win=win, name='StimuliTimer2',
    text='',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Stimuli2 = visual.ImageStim(
    win=win,
    name='Stimuli2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
TR_Stim2 = keyboard.Keyboard()
oddball2 = keyboard.Keyboard()
fixation_cross_4 = visual.ShapeStim(
    win=win, name='fixation_cross_4', vertices='cross',
    size=(0.025, 0.025),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "Stimulus3" ---
StimuliTimer3 = visual.TextStim(win=win, name='StimuliTimer3',
    text='',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Stimuli3 = visual.ImageStim(
    win=win,
    name='Stimuli3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
TR_Stim3 = keyboard.Keyboard()
oddball3 = keyboard.Keyboard()
fixation_cross_5 = visual.ShapeStim(
    win=win, name='fixation_cross_5', vertices='cross',
    size=(0.025, 0.025),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "Stimulus4" ---
StimuliTimer4 = visual.TextStim(win=win, name='StimuliTimer4',
    text='',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Stimuli4 = visual.ImageStim(
    win=win,
    name='Stimuli4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
TR_Stim4 = keyboard.Keyboard()
oddball4 = keyboard.Keyboard()
fixation_cross_6 = visual.ShapeStim(
    win=win, name='fixation_cross_6', vertices='cross',
    size=(0.025, 0.025),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "Rest15secs" ---
text_8 = visual.TextStim(win=win, name='text_8',
    text='Scanner Resting',
    font='Open Sans',
    pos=(0,-0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='',
    font='Open Sans',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
rest_key = keyboard.Keyboard()
fixation_cross_7 = visual.ShapeStim(
    win=win, name='fixation_cross_7', vertices='cross',
    size=(0.025, 0.025),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "routine_5TR_PrePeriod" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
waiting_TR.keys = []
waiting_TR.rt = []
_waiting_TR_allKeys = []
# keep track of which components have finished
routine_5TR_PrePeriodComponents = [waiting_TR, text, fixation_cross]
for thisComponent in routine_5TR_PrePeriodComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "routine_5TR_PrePeriod" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *waiting_TR* updates
    waitOnFlip = False
    if waiting_TR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        waiting_TR.frameNStart = frameN  # exact frame index
        waiting_TR.tStart = t  # local t and not account for scr refresh
        waiting_TR.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(waiting_TR, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'waiting_TR.started')
        waiting_TR.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(waiting_TR.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(waiting_TR.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if waiting_TR.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > waiting_TR.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            waiting_TR.tStop = t  # not accounting for scr refresh
            waiting_TR.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'waiting_TR.stopped')
            waiting_TR.status = FINISHED
    if waiting_TR.status == STARTED and not waitOnFlip:
        theseKeys = waiting_TR.getKeys(keyList=['5'], waitRelease=False)
        _waiting_TR_allKeys.extend(theseKeys)
        if len(_waiting_TR_allKeys):
            waiting_TR.keys = [key.name for key in _waiting_TR_allKeys]  # storing all keys
            waiting_TR.rt = [key.rt for key in _waiting_TR_allKeys]
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            text.setAutoDraw(False)
    # Run 'Each Frame' code from code
    if len (waiting_TR.keys) == 5:
        for i in waiting_TR.keys:
            counter_list.append(counter)
            counter = counter+1
        thisExp2.addData('condition', scanner_msg)    
        thisExp2.addData('TR counter', counter_list)
        thisExp2.nextEntry()
        counter_list=[]
        continueRoutine = False
                
    
    
    # *fixation_cross* updates
    if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_cross.frameNStart = frameN  # exact frame index
        fixation_cross.tStart = t  # local t and not account for scr refresh
        fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation_cross.started')
        fixation_cross.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_5TR_PrePeriodComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "routine_5TR_PrePeriod" ---
for thisComponent in routine_5TR_PrePeriodComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if waiting_TR.keys in ['', [], None]:  # No response was made
    waiting_TR.keys = None
thisExp.addData('waiting_TR.keys',waiting_TR.keys)
if waiting_TR.keys != None:  # we had a response
    thisExp.addData('waiting_TR.rt', waiting_TR.rt)
thisExp.nextEntry()
# the Routine "routine_5TR_PrePeriod" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Conditions.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Prompt" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Prompt1TR.keys = []
    Prompt1TR.rt = []
    _Prompt1TR_allKeys = []
    # Run 'Begin Routine' code from code_4
    condition = trials.thisTrial.get("Condition")
    # keep track of which components have finished
    PromptComponents = [text_9, Prompts, Prompt1TR, fixation_cross_8]
    for thisComponent in PromptComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prompt" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_9.started')
            text_9.setAutoDraw(True)
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_9.stopped')
                text_9.setAutoDraw(False)
        if text_9.status == STARTED:  # only update if drawing
            text_9.setText(t
, log=False)
        
        # *Prompts* updates
        if Prompts.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prompts.frameNStart = frameN  # exact frame index
            Prompts.tStart = t  # local t and not account for scr refresh
            Prompts.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prompts, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Prompts.started')
            Prompts.setAutoDraw(True)
        if Prompts.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Prompts.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Prompts.tStop = t  # not accounting for scr refresh
                Prompts.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Prompts.stopped')
                Prompts.setAutoDraw(False)
        if Prompts.status == STARTED:  # only update if drawing
            Prompts.setImage(Prompt, log=False)
        
        # *Prompt1TR* updates
        waitOnFlip = False
        if Prompt1TR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prompt1TR.frameNStart = frameN  # exact frame index
            Prompt1TR.tStart = t  # local t and not account for scr refresh
            Prompt1TR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prompt1TR, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Prompt1TR.started')
            Prompt1TR.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Prompt1TR.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Prompt1TR.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Prompt1TR.status == STARTED and not waitOnFlip:
            theseKeys = Prompt1TR.getKeys(keyList=['5'], waitRelease=False)
            _Prompt1TR_allKeys.extend(theseKeys)
            if len(_Prompt1TR_allKeys):
                Prompt1TR.keys = [key.name for key in _Prompt1TR_allKeys]  # storing all keys
                Prompt1TR.rt = [key.rt for key in _Prompt1TR_allKeys]
        # Run 'Each Frame' code from code_4
        if len (Prompt1TR.keys) == 1:
                    for i in Prompt1TR.keys:
                        counter_list.append(counter)
                        counter = counter+1
                        
                    thisExp2.addData('condition',condition+"_Prompt")    
                    thisExp2.addData('TR counter',counter_list)
                    thisExp2.nextEntry()
                    counter_list=[]
                    continueRoutine = False
        
        # *fixation_cross_8* updates
        if fixation_cross_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross_8.frameNStart = frameN  # exact frame index
            fixation_cross_8.tStart = t  # local t and not account for scr refresh
            fixation_cross_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_cross_8.started')
            fixation_cross_8.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PromptComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prompt" ---
    for thisComponent in PromptComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Prompt1TR.keys in ['', [], None]:  # No response was made
        Prompt1TR.keys = None
    trials.addData('Prompt1TR.keys',Prompt1TR.keys)
    if Prompt1TR.keys != None:  # we had a response
        trials.addData('Prompt1TR.rt', Prompt1TR.rt)
    # the Routine "Prompt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "RestEither3or6Secs" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text_2.setText('\n')
    # Run 'Begin Routine' code from code_3
    jitter = trials.thisTrial.get("TimeBetween")
    
    
    
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    RestEither3or6SecsComponents = [text_2, text_10, key_resp, fixation_cross_2]
    for thisComponent in RestEither3or6SecsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "RestEither3or6Secs" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_10.started')
            text_10.setAutoDraw(True)
        if text_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_10.tStartRefresh + TimeBetween-frameTolerance:
                # keep track of stop time/frame for later
                text_10.tStop = t  # not accounting for scr refresh
                text_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_10.stopped')
                text_10.setAutoDraw(False)
        if text_10.status == STARTED:  # only update if drawing
            text_10.setText(t, log=False)
        # Run 'Each Frame' code from code_3
        if jitter == 1.5:
            if len (key_resp.keys) == 1:
                counter_list.append(counter)
                counter = counter+1
                thisExp2.addData('condition', condition+"_Jitter")    
                thisExp2.addData('TR counter',counter_list)
                thisExp2.addData('Jitter Time',jitter)
                thisExp2.nextEntry()
                counter_list = []
                continueRoutine = False
        if jitter == 3.0:
            if len (key_resp.keys) == 2:
                for i in key_resp.keys:
                        counter_list.append(counter)
                        counter = counter+1
                thisExp2.addData('condition',condition+"_Jitter")    
                thisExp2.addData('TR counter',counter_list)
                thisExp2.addData('Jitter Time',jitter)
                thisExp2.nextEntry()
                counter_list = []
                continueRoutine = False
        if jitter == 4.5:
            if len (key_resp.keys) == 3:
                for i in key_resp.keys:
                        counter_list.append(counter)
                        counter = counter+1
                thisExp2.addData('condition',condition+"_Jitter")    
                thisExp2.addData('TR counter',counter_list)
                thisExp2.addData('Jitter Time',jitter)
                thisExp2.nextEntry()
                counter_list = []
                continueRoutine = False
                    
        
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['5'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                key_resp.rt = [key.rt for key in _key_resp_allKeys]
        
        # *fixation_cross_2* updates
        if fixation_cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross_2.frameNStart = frameN  # exact frame index
            fixation_cross_2.tStart = t  # local t and not account for scr refresh
            fixation_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_cross_2.started')
            fixation_cross_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RestEither3or6SecsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RestEither3or6Secs" ---
    for thisComponent in RestEither3or6SecsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    # the Routine "RestEither3or6Secs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Stimulus1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    TR_Stim1.keys = []
    TR_Stim1.rt = []
    _TR_Stim1_allKeys = []
    oddball1.keys = []
    oddball1.rt = []
    _oddball1_allKeys = []
    # keep track of which components have finished
    Stimulus1Components = [StimuliTimer1, Stimuli1, TR_Stim1, oddball1, fixation_cross_3]
    for thisComponent in Stimulus1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Stimulus1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StimuliTimer1* updates
        if StimuliTimer1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StimuliTimer1.frameNStart = frameN  # exact frame index
            StimuliTimer1.tStart = t  # local t and not account for scr refresh
            StimuliTimer1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StimuliTimer1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StimuliTimer1.started')
            StimuliTimer1.setAutoDraw(True)
        if StimuliTimer1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StimuliTimer1.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                StimuliTimer1.tStop = t  # not accounting for scr refresh
                StimuliTimer1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StimuliTimer1.stopped')
                StimuliTimer1.setAutoDraw(False)
        if StimuliTimer1.status == STARTED:  # only update if drawing
            StimuliTimer1.setText(t, log=False)
        
        # *Stimuli1* updates
        if Stimuli1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stimuli1.frameNStart = frameN  # exact frame index
            Stimuli1.tStart = t  # local t and not account for scr refresh
            Stimuli1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Stimuli1.started')
            Stimuli1.setAutoDraw(True)
        if Stimuli1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stimuli1.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Stimuli1.tStop = t  # not accounting for scr refresh
                Stimuli1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stimuli1.stopped')
                Stimuli1.setAutoDraw(False)
        if Stimuli1.status == STARTED:  # only update if drawing
            Stimuli1.setImage(Stim1, log=False)
        
        # *TR_Stim1* updates
        waitOnFlip = False
        if TR_Stim1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TR_Stim1.frameNStart = frameN  # exact frame index
            TR_Stim1.tStart = t  # local t and not account for scr refresh
            TR_Stim1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TR_Stim1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TR_Stim1.started')
            TR_Stim1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(TR_Stim1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(TR_Stim1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if TR_Stim1.status == STARTED and not waitOnFlip:
            theseKeys = TR_Stim1.getKeys(keyList=['5'], waitRelease=False)
            _TR_Stim1_allKeys.extend(theseKeys)
            if len(_TR_Stim1_allKeys):
                TR_Stim1.keys = [key.name for key in _TR_Stim1_allKeys]  # storing all keys
                TR_Stim1.rt = [key.rt for key in _TR_Stim1_allKeys]
        # Run 'Each Frame' code from code_5
        if len (TR_Stim1.keys) == 1:
                    for i in TR_Stim1.keys:
                        counter_list.append(counter)
                        counter = counter+1
                        
                        
                    thisExp2.addData('condition',condition+"_Stim1")    
                    thisExp2.addData('TR counter',counter_list)
                    thisExp2.addData('oddball',oddball1.keys)
                    thisExp2.nextEntry()
                    counter_list=[]
                    continueRoutine = False
        
        # *oddball1* updates
        waitOnFlip = False
        if oddball1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            oddball1.frameNStart = frameN  # exact frame index
            oddball1.tStart = t  # local t and not account for scr refresh
            oddball1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(oddball1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'oddball1.started')
            oddball1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(oddball1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(oddball1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if oddball1.status == STARTED and not waitOnFlip:
            theseKeys = oddball1.getKeys(keyList=['1'], waitRelease=False)
            _oddball1_allKeys.extend(theseKeys)
            if len(_oddball1_allKeys):
                oddball1.keys = [key.name for key in _oddball1_allKeys]  # storing all keys
                oddball1.rt = [key.rt for key in _oddball1_allKeys]
        
        # *fixation_cross_3* updates
        if fixation_cross_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross_3.frameNStart = frameN  # exact frame index
            fixation_cross_3.tStart = t  # local t and not account for scr refresh
            fixation_cross_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_cross_3.started')
            fixation_cross_3.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Stimulus1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Stimulus1" ---
    for thisComponent in Stimulus1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if TR_Stim1.keys in ['', [], None]:  # No response was made
        TR_Stim1.keys = None
    trials.addData('TR_Stim1.keys',TR_Stim1.keys)
    if TR_Stim1.keys != None:  # we had a response
        trials.addData('TR_Stim1.rt', TR_Stim1.rt)
    # check responses
    if oddball1.keys in ['', [], None]:  # No response was made
        oddball1.keys = None
    trials.addData('oddball1.keys',oddball1.keys)
    if oddball1.keys != None:  # we had a response
        trials.addData('oddball1.rt', oddball1.rt)
    # the Routine "Stimulus1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Stimulus2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    TR_Stim2.keys = []
    TR_Stim2.rt = []
    _TR_Stim2_allKeys = []
    oddball2.keys = []
    oddball2.rt = []
    _oddball2_allKeys = []
    # keep track of which components have finished
    Stimulus2Components = [StimuliTimer2, Stimuli2, TR_Stim2, oddball2, fixation_cross_4]
    for thisComponent in Stimulus2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Stimulus2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StimuliTimer2* updates
        if StimuliTimer2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StimuliTimer2.frameNStart = frameN  # exact frame index
            StimuliTimer2.tStart = t  # local t and not account for scr refresh
            StimuliTimer2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StimuliTimer2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StimuliTimer2.started')
            StimuliTimer2.setAutoDraw(True)
        if StimuliTimer2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StimuliTimer2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                StimuliTimer2.tStop = t  # not accounting for scr refresh
                StimuliTimer2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StimuliTimer2.stopped')
                StimuliTimer2.setAutoDraw(False)
        if StimuliTimer2.status == STARTED:  # only update if drawing
            StimuliTimer2.setText(t, log=False)
        
        # *Stimuli2* updates
        if Stimuli2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stimuli2.frameNStart = frameN  # exact frame index
            Stimuli2.tStart = t  # local t and not account for scr refresh
            Stimuli2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Stimuli2.started')
            Stimuli2.setAutoDraw(True)
        if Stimuli2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stimuli2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Stimuli2.tStop = t  # not accounting for scr refresh
                Stimuli2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stimuli2.stopped')
                Stimuli2.setAutoDraw(False)
        if Stimuli2.status == STARTED:  # only update if drawing
            Stimuli2.setImage(Stim2, log=False)
        
        # *TR_Stim2* updates
        waitOnFlip = False
        if TR_Stim2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TR_Stim2.frameNStart = frameN  # exact frame index
            TR_Stim2.tStart = t  # local t and not account for scr refresh
            TR_Stim2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TR_Stim2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TR_Stim2.started')
            TR_Stim2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(TR_Stim2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(TR_Stim2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if TR_Stim2.status == STARTED and not waitOnFlip:
            theseKeys = TR_Stim2.getKeys(keyList=['5'], waitRelease=False)
            _TR_Stim2_allKeys.extend(theseKeys)
            if len(_TR_Stim2_allKeys):
                TR_Stim2.keys = [key.name for key in _TR_Stim2_allKeys]  # storing all keys
                TR_Stim2.rt = [key.rt for key in _TR_Stim2_allKeys]
        # Run 'Each Frame' code from code_6
        if len (TR_Stim2.keys) == 1:
                    for i in TR_Stim2.keys:
                        counter_list.append(counter)
                        counter = counter+1
                    thisExp2.addData('condition',condition+"_Stim2")    
                    thisExp2.addData('TR counter',counter_list)
                    thisExp2.addData('oddball',oddball2.keys)
                    thisExp2.nextEntry()
                    counter_list=[]
                    continueRoutine = False
        
        # *oddball2* updates
        waitOnFlip = False
        if oddball2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            oddball2.frameNStart = frameN  # exact frame index
            oddball2.tStart = t  # local t and not account for scr refresh
            oddball2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(oddball2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'oddball2.started')
            oddball2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(oddball2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(oddball2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if oddball2.status == STARTED and not waitOnFlip:
            theseKeys = oddball2.getKeys(keyList=['1'], waitRelease=False)
            _oddball2_allKeys.extend(theseKeys)
            if len(_oddball2_allKeys):
                oddball2.keys = [key.name for key in _oddball2_allKeys]  # storing all keys
                oddball2.rt = [key.rt for key in _oddball2_allKeys]
        
        # *fixation_cross_4* updates
        if fixation_cross_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross_4.frameNStart = frameN  # exact frame index
            fixation_cross_4.tStart = t  # local t and not account for scr refresh
            fixation_cross_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_cross_4.started')
            fixation_cross_4.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Stimulus2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Stimulus2" ---
    for thisComponent in Stimulus2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if TR_Stim2.keys in ['', [], None]:  # No response was made
        TR_Stim2.keys = None
    trials.addData('TR_Stim2.keys',TR_Stim2.keys)
    if TR_Stim2.keys != None:  # we had a response
        trials.addData('TR_Stim2.rt', TR_Stim2.rt)
    # check responses
    if oddball2.keys in ['', [], None]:  # No response was made
        oddball2.keys = None
    trials.addData('oddball2.keys',oddball2.keys)
    if oddball2.keys != None:  # we had a response
        trials.addData('oddball2.rt', oddball2.rt)
    # the Routine "Stimulus2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Stimulus3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    TR_Stim3.keys = []
    TR_Stim3.rt = []
    _TR_Stim3_allKeys = []
    oddball3.keys = []
    oddball3.rt = []
    _oddball3_allKeys = []
    # keep track of which components have finished
    Stimulus3Components = [StimuliTimer3, Stimuli3, TR_Stim3, oddball3, fixation_cross_5]
    for thisComponent in Stimulus3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Stimulus3" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StimuliTimer3* updates
        if StimuliTimer3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StimuliTimer3.frameNStart = frameN  # exact frame index
            StimuliTimer3.tStart = t  # local t and not account for scr refresh
            StimuliTimer3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StimuliTimer3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StimuliTimer3.started')
            StimuliTimer3.setAutoDraw(True)
        if StimuliTimer3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StimuliTimer3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                StimuliTimer3.tStop = t  # not accounting for scr refresh
                StimuliTimer3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StimuliTimer3.stopped')
                StimuliTimer3.setAutoDraw(False)
        if StimuliTimer3.status == STARTED:  # only update if drawing
            StimuliTimer3.setText(t, log=False)
        
        # *Stimuli3* updates
        if Stimuli3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stimuli3.frameNStart = frameN  # exact frame index
            Stimuli3.tStart = t  # local t and not account for scr refresh
            Stimuli3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Stimuli3.started')
            Stimuli3.setAutoDraw(True)
        if Stimuli3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stimuli3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Stimuli3.tStop = t  # not accounting for scr refresh
                Stimuli3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stimuli3.stopped')
                Stimuli3.setAutoDraw(False)
        if Stimuli3.status == STARTED:  # only update if drawing
            Stimuli3.setImage(Stim3, log=False)
        
        # *TR_Stim3* updates
        waitOnFlip = False
        if TR_Stim3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TR_Stim3.frameNStart = frameN  # exact frame index
            TR_Stim3.tStart = t  # local t and not account for scr refresh
            TR_Stim3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TR_Stim3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TR_Stim3.started')
            TR_Stim3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(TR_Stim3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(TR_Stim3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if TR_Stim3.status == STARTED and not waitOnFlip:
            theseKeys = TR_Stim3.getKeys(keyList=['5'], waitRelease=False)
            _TR_Stim3_allKeys.extend(theseKeys)
            if len(_TR_Stim3_allKeys):
                TR_Stim3.keys = _TR_Stim3_allKeys[-1].name  # just the last key pressed
                TR_Stim3.rt = _TR_Stim3_allKeys[-1].rt
        # Run 'Each Frame' code from code_7
        if len (TR_Stim3.keys) == 1:
                    for i in TR_Stim3.keys:
                        counter_list.append(counter)
                        counter = counter+1
                    thisExp2.addData('condition', condition+"_Stim3")    
                    thisExp2.addData('TR counter',counter_list)
                    thisExp2.addData('oddball',oddball3.keys)
                    thisExp2.nextEntry()
                    counter_list=[]
                    continueRoutine = False
        
        # *oddball3* updates
        waitOnFlip = False
        if oddball3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            oddball3.frameNStart = frameN  # exact frame index
            oddball3.tStart = t  # local t and not account for scr refresh
            oddball3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(oddball3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'oddball3.started')
            oddball3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(oddball3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(oddball3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if oddball3.status == STARTED and not waitOnFlip:
            theseKeys = oddball3.getKeys(keyList=['1'], waitRelease=False)
            _oddball3_allKeys.extend(theseKeys)
            if len(_oddball3_allKeys):
                oddball3.keys = [key.name for key in _oddball3_allKeys]  # storing all keys
                oddball3.rt = [key.rt for key in _oddball3_allKeys]
        
        # *fixation_cross_5* updates
        if fixation_cross_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross_5.frameNStart = frameN  # exact frame index
            fixation_cross_5.tStart = t  # local t and not account for scr refresh
            fixation_cross_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_cross_5.started')
            fixation_cross_5.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Stimulus3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Stimulus3" ---
    for thisComponent in Stimulus3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if TR_Stim3.keys in ['', [], None]:  # No response was made
        TR_Stim3.keys = None
    trials.addData('TR_Stim3.keys',TR_Stim3.keys)
    if TR_Stim3.keys != None:  # we had a response
        trials.addData('TR_Stim3.rt', TR_Stim3.rt)
    # check responses
    if oddball3.keys in ['', [], None]:  # No response was made
        oddball3.keys = None
    trials.addData('oddball3.keys',oddball3.keys)
    if oddball3.keys != None:  # we had a response
        trials.addData('oddball3.rt', oddball3.rt)
    # the Routine "Stimulus3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Stimulus4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    TR_Stim4.keys = []
    TR_Stim4.rt = []
    _TR_Stim4_allKeys = []
    oddball4.keys = []
    oddball4.rt = []
    _oddball4_allKeys = []
    # keep track of which components have finished
    Stimulus4Components = [StimuliTimer4, Stimuli4, TR_Stim4, oddball4, fixation_cross_6]
    for thisComponent in Stimulus4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Stimulus4" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StimuliTimer4* updates
        if StimuliTimer4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StimuliTimer4.frameNStart = frameN  # exact frame index
            StimuliTimer4.tStart = t  # local t and not account for scr refresh
            StimuliTimer4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StimuliTimer4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StimuliTimer4.started')
            StimuliTimer4.setAutoDraw(True)
        if StimuliTimer4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StimuliTimer4.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                StimuliTimer4.tStop = t  # not accounting for scr refresh
                StimuliTimer4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StimuliTimer4.stopped')
                StimuliTimer4.setAutoDraw(False)
        if StimuliTimer4.status == STARTED:  # only update if drawing
            StimuliTimer4.setText(t, log=False)
        
        # *Stimuli4* updates
        if Stimuli4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stimuli4.frameNStart = frameN  # exact frame index
            Stimuli4.tStart = t  # local t and not account for scr refresh
            Stimuli4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Stimuli4.started')
            Stimuli4.setAutoDraw(True)
        if Stimuli4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stimuli4.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Stimuli4.tStop = t  # not accounting for scr refresh
                Stimuli4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stimuli4.stopped')
                Stimuli4.setAutoDraw(False)
        if Stimuli4.status == STARTED:  # only update if drawing
            Stimuli4.setImage(Stim4, log=False)
        
        # *TR_Stim4* updates
        waitOnFlip = False
        if TR_Stim4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TR_Stim4.frameNStart = frameN  # exact frame index
            TR_Stim4.tStart = t  # local t and not account for scr refresh
            TR_Stim4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TR_Stim4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TR_Stim4.started')
            TR_Stim4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(TR_Stim4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(TR_Stim4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if TR_Stim4.status == STARTED and not waitOnFlip:
            theseKeys = TR_Stim4.getKeys(keyList=['5'], waitRelease=False)
            _TR_Stim4_allKeys.extend(theseKeys)
            if len(_TR_Stim4_allKeys):
                TR_Stim4.keys = _TR_Stim4_allKeys[-1].name  # just the last key pressed
                TR_Stim4.rt = _TR_Stim4_allKeys[-1].rt
        # Run 'Each Frame' code from code_8
        if len (TR_Stim4.keys) == 1:
                    for i in TR_Stim4.keys:
                        counter_list.append(counter)
                        counter = counter+1
                    thisExp2.addData('condition',condition+"_Stim4")    
                    thisExp2.addData('TR counter',counter_list)
                    thisExp2.addData('oddball',oddball4.keys)
                    thisExp2.nextEntry()
                    counter_list=[]
                    continueRoutine = False
        
        # *oddball4* updates
        waitOnFlip = False
        if oddball4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            oddball4.frameNStart = frameN  # exact frame index
            oddball4.tStart = t  # local t and not account for scr refresh
            oddball4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(oddball4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'oddball4.started')
            oddball4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(oddball4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(oddball4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if oddball4.status == STARTED and not waitOnFlip:
            theseKeys = oddball4.getKeys(keyList=['1'], waitRelease=False)
            _oddball4_allKeys.extend(theseKeys)
            if len(_oddball4_allKeys):
                oddball4.keys = [key.name for key in _oddball4_allKeys]  # storing all keys
                oddball4.rt = [key.rt for key in _oddball4_allKeys]
        
        # *fixation_cross_6* updates
        if fixation_cross_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross_6.frameNStart = frameN  # exact frame index
            fixation_cross_6.tStart = t  # local t and not account for scr refresh
            fixation_cross_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_cross_6.started')
            fixation_cross_6.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Stimulus4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Stimulus4" ---
    for thisComponent in Stimulus4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if TR_Stim4.keys in ['', [], None]:  # No response was made
        TR_Stim4.keys = None
    trials.addData('TR_Stim4.keys',TR_Stim4.keys)
    if TR_Stim4.keys != None:  # we had a response
        trials.addData('TR_Stim4.rt', TR_Stim4.rt)
    # check responses
    if oddball4.keys in ['', [], None]:  # No response was made
        oddball4.keys = None
    trials.addData('oddball4.keys',oddball4.keys)
    if oddball4.keys != None:  # we had a response
        trials.addData('oddball4.rt', oddball4.rt)
    # the Routine "Stimulus4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Rest15secs" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    condition = "rest_scanner"
    rest_key.keys = []
    rest_key.rt = []
    _rest_key_allKeys = []
    # keep track of which components have finished
    Rest15secsComponents = [text_8, text_15, rest_key, fixation_cross_7]
    for thisComponent in Rest15secsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Rest15secs" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_8.started')
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_8.stopped')
                text_8.setAutoDraw(False)
        
        # *text_15* updates
        if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_15.frameNStart = frameN  # exact frame index
            text_15.tStart = t  # local t and not account for scr refresh
            text_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_15.started')
            text_15.setAutoDraw(True)
        if text_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_15.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_15.tStop = t  # not accounting for scr refresh
                text_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_15.stopped')
                text_15.setAutoDraw(False)
        if text_15.status == STARTED:  # only update if drawing
            text_15.setText(t, log=False)
        # Run 'Each Frame' code from code_2
        if len (rest_key.keys) == 8:
            for i in rest_key.keys:
                counter_list.append(counter)
                counter = counter+1   
            thisExp2.addData('condition',condition)    
            thisExp2.addData('TR counter',counter_list)
            thisExp2.nextEntry()
            counter_list = []
            continueRoutine = False
                    
        
        # *rest_key* updates
        waitOnFlip = False
        if rest_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_key.frameNStart = frameN  # exact frame index
            rest_key.tStart = t  # local t and not account for scr refresh
            rest_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_key.started')
            rest_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rest_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rest_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rest_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_key.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                rest_key.tStop = t  # not accounting for scr refresh
                rest_key.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_key.stopped')
                rest_key.status = FINISHED
        if rest_key.status == STARTED and not waitOnFlip:
            theseKeys = rest_key.getKeys(keyList=['5'], waitRelease=False)
            _rest_key_allKeys.extend(theseKeys)
            if len(_rest_key_allKeys):
                rest_key.keys = [key.name for key in _rest_key_allKeys]  # storing all keys
                rest_key.rt = [key.rt for key in _rest_key_allKeys]
        
        # *fixation_cross_7* updates
        if fixation_cross_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross_7.frameNStart = frameN  # exact frame index
            fixation_cross_7.tStart = t  # local t and not account for scr refresh
            fixation_cross_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_cross_7.started')
            fixation_cross_7.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Rest15secsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Rest15secs" ---
    for thisComponent in Rest15secsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if rest_key.keys in ['', [], None]:  # No response was made
        rest_key.keys = None
    trials.addData('rest_key.keys',rest_key.keys)
    if rest_key.keys != None:  # we had a response
        trials.addData('rest_key.rt', rest_key.rt)
    # the Routine "Rest15secs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
