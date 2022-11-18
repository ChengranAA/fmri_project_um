"""
=======================================================
Title: Hebb repetition task and serial recognition task
Author: Chengran Li
=======================================================

Experiment schdule:
- Welcome
- Audio check
- Instruction
- Practice
- HRE experiment
- Passive listening test

# TODO:
- Timing information
- Data storing
- EEG marker (serial port)
-
"""
from psychopy import core, visual, gui, data, event, sound, prefs, clock
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

# serial port connection
"""
ser = serial.Serial(0, )
"""
# load the trigger file
triggers = data.importConditions('Resource'+file_sep+'trigger.csv')
trigger_key = ["FillerOnset1","FillerOffset1","HebbOnset2","HebbOffset2","FillerOnset3","FillerOffset3","HebbOnset4","HebbOfffset4"]

# set the prefer sound engine to Psycho tool box
prefs.hardware['audioLib'] = ['PTB']

# add global shutdown key 'escape'
event.globalKeys.add(key='escape', func=core.quit, name='shutdown')

# setting up dialogue gui
expInfo = {'participant':'', 'session': '001'}
expInfo['Date'] = data.getDateStr()

# present a gui for user
dlg = gui.DlgFromDict(expInfo, title='Hello', fixed=['dateStr'])
if dlg.OK == False:
    core.quit()

# make a text file to save data

if os.path.isdir('Data') == False: # check if data file is exist, if not create one
    os.mkdir('Data')
if os.path.isdir('Data'+file_sep+'Practice') == False:
    os.mkdir('Data'+file_sep+'Practice')
if os.path.isdir('Data'+file_sep+'HRT') == False:
    os.mkdir('Data'+file_sep+'HRT')
if os.path.isdir('Data'+file_sep+'SRT') == False:
    os.mkdir('Data'+file_sep+'SRT')
fileName = expInfo['participant']+'_'+ expInfo['Date']

# setting up experiment Handler
exp_HRT = data.ExperimentHandler(name="HRT Paradigm", version='0.1.0', extraInfo=expInfo, dataFileName='Data'+file_sep+'HRT'+file_sep+''+fileName+'_'+'HRT') # Hebb repetition task
exp_practice = data.ExperimentHandler(name="HRT Paradigm practice", version='0.1.0', extraInfo=expInfo, dataFileName='Data'+file_sep+'Practice'+file_sep+''+fileName+'_'+'practice') # Hebb repetition task practice
exp_SRT = data.ExperimentHandler(name="SRT Paradigm", version='0.1.0', extraInfo=expInfo, dataFileName='Data'+file_sep+'SRT'+file_sep+''+fileName+'_'+'SRT') # serial recognition task

## initialise Window
win = visual.Window([1920,1080],allowGUI=True, monitor='testMonitor', units='pix', fullscr=True)

## global component
mouse = event.Mouse()
win.mouseVisible = False
mouse.setPos(newPos=(700,-500))

fixation = visual.ShapeStim(win, pos=[0,0],
                            vertices=((0, -30), (0, 30), (0,0), (-30,0), (30, 0)),
                            lineWidth=5,
                            closeShape=False,
                            lineColor="white")
# counter
counter_txt = visual.TextStim(win, pos=[-700,400], height=40, text="0/9", color=[1,1,1], units='pix')

# circle_1
circle_1_txt = visual.TextStim(win, pos=[0,360], height=50, text='1', color=[1,1,1], units='pix')
circle_1 = visual.Circle(win, pos=[0,360], radius=50, edges=50, units='pix')
# circle_2
circle_2_txt = visual.TextStim(win, pos=[240,240], height=50, text='2', color=[1,1,1], units='pix')
circle_2 = visual.Circle(win, pos=[240,240], radius=50, edges=50, units='pix')
# circle_3
circle_3_txt = visual.TextStim(win, pos=[360,60], height=50, text='3', color=[1,1,1], units='pix')
circle_3 = visual.Circle(win, pos=[360,60], radius=50, edges=50, units='pix')
# circle_4
circle_4_txt = visual.TextStim(win, pos=[280,-140], height=50, text='4', color=[1,1,1], units='pix')
circle_4 = visual.Circle(win, pos=[280,-140], radius=50, edges=50, units='pix')
# circle_5
circle_5_txt = visual.TextStim(win, pos=[110,-300], height=50, text='5', color=[1,1,1], units='pix')
circle_5 = visual.Circle(win, pos=[110,-300], radius=50, edges=50, units='pix')
# circle_6
circle_6_txt = visual.TextStim(win, pos=[-110,-300], height=50, text='6', color=[1,1,1], units='pix')
circle_6 = visual.Circle(win, pos=[-110,-300], radius=50, edges=50, units='pix')
# circle_7
circle_7_txt = visual.TextStim(win, pos=[-280,-140], height=50, text='7', color=[1,1,1], units='pix')
circle_7 = visual.Circle(win, pos=[-280,-140], radius=50, edges=50, units='pix')
# circle_8
circle_8_txt = visual.TextStim(win, pos=[-360,60], height=50, text='8', color=[1,1,1], units='pix')
circle_8 = visual.Circle(win, pos=[-360,60], radius=50, edges=50, units='pix')
# circle_9
circle_9_txt = visual.TextStim(win, pos=[-240,240], height=50, text='9', color=[1,1,1], units='pix')
circle_9 = visual.Circle(win, pos=[-240,240], radius=50, edges=50, units='pix')
# circle_question
circle_question_txt = visual.TextStim(win, pos=[0,0], height=50, text='?', color=[1,1,1], units='pix')
circle_question = visual.Circle(win, pos=[0,0], radius=50, edges=50, units='pix')

# circle and cricle text lists
circles = [circle_1, circle_2, circle_3, circle_4, circle_5,circle_6,circle_7,circle_8, circle_9, circle_question]
circles_txt = [circle_1_txt, circle_2_txt, circle_3_txt, circle_4_txt, circle_5_txt,circle_6_txt,circle_7_txt,circle_8_txt, circle_9_txt, circle_question_txt]

# global variable
sound_file_prefix = 'Resource'+file_sep+'CV'+file_sep

## <Welcome window>
# initialise welcome window components
welcome_txt_1 = visual.TextStim(win, pos=[0,0], height=80, text='Welcome to the experiment')
welcome_txt_2 = visual.TextStim(win, pos=[0,-400],height=30, text="<Press any key to continue>")

welcome_txt_1.draw()
welcome_txt_2.draw()
win.flip()
event.waitKeys()

## <Check Audio>
# initialise check  component
check_instr = visual.TextStim(win, pos=[0,0],
                              height=50, text = """This is an audio check to ensure your volume is working for the experiment.You are going to hear a series of sounds.
                                                Please ensure your speakers are at a comfortable listening volume. If you are unable to hear the sounds,
                                                contact your experimenter immediately and press esc to end the experiment
                                                <Press the spacebar to continue>.""", alignText = 'left')
check_instr.wrapWidth = 1200
check_con = data.importConditions('Resource'+file_sep+'checkloops.csv')
check_audio = sound.Sound(stereo=True)
check_txt = visual.TextStim(win, pos=[0,0], height=100,
                            text='')
check_end = visual.TextStim(win, pos=[0,0], height=50,
                            text='If you have no problem with the audio test press any key to continue')
check_end.wrapWidth = 1200

# start Check Audio
# check instruction
check_instr.draw()
win.flip()
event.waitKeys(keyList=['space'])

# check audio loop
for checkT in range(3):
    heck_seq = list()
    check_con_seq = np.random.choice(check_con, size=4, replace=False)
    for checkSeqT in range(4):
        check_audio.setSound('Resource'+file_sep+'audio-test'+file_sep+ check_con_seq[checkSeqT]['checkfile'][:-4])
        check_txt.text = check_con_seq[checkSeqT]['checkfile'][:-4]
        check_txt.draw()
        win.flip()
        now = ptb.GetSecs()
        check_audio.play(when=now)
        core.wait(1)
    if checkT < 2:
        fixation.draw()
        win.flip()
        core.wait(1)
check_end.draw()
win.flip()
event.waitKeys()

## <Instruction>
# initialise instruction components
instruc_txt = visual.TextStim(win, pos=[0,0], height=50, text=" In this experiment, you are going to hear and see a series of sounds. \
                                                                Once the sounds stop playing, you will be instructed to order them in exactly the order you heard them in by using your mouse to click each sound. \
                                                                You must click all nine sounds before completing a trial.\
                                                                If you are unsure of the ordering at any point, click the question mark in the middle of the screen for that item. \
                                                                You may click the question mark for any number of items you are unsure of.\
                                                                You will complete some practice trials, and then the real test will begin. \
                                                                Press the spacebar to continue.", alignText = 'left')
instruc_txt.wrapWidth = 1200
# start Instruction
instruc_txt.draw()
win.flip()
event.waitKeys()


fixation.draw()
win.flip()
t = clock.getTime()
exp_practice.addData("practice_trial.onset", t)
core.wait(0.5)

## <HRE Experiment Trial>
# initialise HRE Experiment trial components
HRE_txt = visual.TextStim(win, pos=[0,0], height=100, text='')
HRE_audio = sound.Sound(stereo=True)


# prepare the practice list
practice_con_file = data.importConditions('Resource'+file_sep+'HRE_Practice_Trials.csv')
practice_trial = data.TrialHandler(trialList=practice_con_file, nReps=1, method = 'sequential')

# start the practice test
for eachTrial in practice_trial:
    eachTrial.pop("Trial")  # pop the unecessary info
    seq_list = list() # sequence list
    seq_num = 0 # cv counter
    mem_test_num = 0 # sequence counter
    for key,value in eachTrial.items():
        # store the vlaue to the list
        seq_list.append(value)
        seq_num += 1
        # set sound and text for CVs
        HRE_audio.setSound(sound_file_prefix + str(value))
        HRE_txt.text = str(value[:-4])
        # play sound and show the CV text
        HRE_txt.draw()
        now = ptb.GetSecs()
        HRE_audio.play(when=now)
        win.flip()
        t = clock.getTime()
        exp_practice.addData(key+".onset", t)
        # each stimuli last 500ms
        core.wait(0.5)
        # if counter reach 9 which mean a full sequence pass
        if seq_num == 9:
            mem_test_num += 1
            # show a fixation for later memory test
            fixation.draw()
            win.flip()
            t = clock.getTime()
            exp_practice.addData("Practice_Mem_test.fixation_"+str(mem_test_num)+".onset", t)
            core.wait(0.5)
            random.shuffle(seq_list) # this randomies the seq_list for memory test
            for index,text in enumerate(circles_txt):
                # the last one in the list is question mark so skip
                if index < 9:
                    # change the rest of the circle text to the item in the shuffled list
                    circles_txt[index].text = str(seq_list[index][:-4])
            list_resp = list()
            clicked_num = 0

            # the memory test at the end of the sequence
            win.mouseVisible = True
            t = clock.getTime()
            exp_practice.addData("Practice_Mem_test_"+str(mem_test_num)+".onset", t)
            while True:
                for n, shape in enumerate(circles):
                    # when
                    if mouse.isPressedIn(shape):
                        clicked_num += 1
                        counter_txt.text = str(clicked_num) + "/9"
                        list_resp.append(circles_txt[n].text)
                        if circles_txt[n].text != '?':
                            del circles[n]
                            del circles_txt[n]
                        core.wait(0.1) # CAUTION: Do not click down mouse for too long, it will count as multiple clicks, can not be solved
                                       #          click time can only be within 100ms

                # if click respones more than 9 times, break out of the memory test
                if clicked_num == 9:
                    mouse.setPos(newPos=(700, -500))
                    break
                # change the text color when hover the text, give the participant an idea of which item they want to presss
                if circle_1.contains(mouse):
                    circle_1_txt.color = [-1,-1,-1]
                elif circle_2.contains(mouse):
                    circle_2_txt.color = [-1,-1,-1]
                elif circle_3.contains(mouse):
                    circle_3_txt.color = [-1,-1,-1]
                elif circle_4.contains(mouse):
                    circle_4_txt.color = [-1,-1,-1]
                elif circle_5.contains(mouse):
                    circle_5_txt.color = [-1,-1,-1]
                elif circle_6.contains(mouse):
                    circle_6_txt.color = [-1,-1,-1]
                elif circle_7.contains(mouse):
                    circle_7_txt.color = [-1,-1,-1]
                elif circle_8.contains(mouse):
                    circle_8_txt.color = [-1,-1,-1]
                elif circle_9.contains(mouse):
                    circle_9_txt.color = [-1,-1,-1]
                elif circle_question.contains(mouse):
                    circle_question_txt.color = [-1,-1,-1]

                # change back the color of the text when not hover
                else:
                    for index, text in enumerate(circles_txt):
                        circles_txt[index].color = [1,1,1]
             # drawing helps visual ize the mechanics
                for index, circle in enumerate(circles):
                    circles[index].draw()
                    circles_txt[index].draw()
                counter_txt.draw()
                win.flip()

            clicked_num = 0 # reset clicked number
            counter_txt.text = str(clicked_num) + "/9" # reset counter

            # reset circle and circle_text list
            circles = [circle_1, circle_2, circle_3, circle_4, circle_5,circle_6,circle_7,circle_8, circle_9, circle_question]
            circles_txt = [circle_1_txt, circle_2_txt, circle_3_txt, circle_4_txt, circle_5_txt,circle_6_txt,circle_7_txt,circle_8_txt, circle_9_txt, circle_question_txt]

            win.mouseVisible = False
            # show fixation point
            fixation.draw()
            win.flip()
            t = clock.getTime()
            exp_practice.addData("Practice_Mem_test.end_fixation_"+str(mem_test_num)+".onset",t)
            core.wait(0.5)

            # print and save the response list
            exp_practice.addData('practice.resp_'+str(mem_test_num), list_resp)

            seq_num = 0 # reset sequence counter
            seq_list = list() # reset sequence list for next list
    exp_practice.nextEntry()

# store the end of the practice tral time
t = core.getTime()
exp_practice.addData('practice_trial.offset',t)

# Practice end screen
practice_end = visual.TextStim(win, pos=[0,0], height=50, text='If you are ready for the actual experiment, press any key to continue.')
practice_end.draw()
win.flip()
event.waitKeys()

# prepare the HRE experiment lists
HRE_con_file = data.importConditions('Resource'+file_sep+'HRE_Experiment_Table.csv')
HRE_trial = data.TrialHandler(trialList=HRE_con_file, nReps=1, method = 'sequential')

# start fixation screen
fixation.draw()
win.flip()
t = clock.getTime()
exp_HRT.addData("HRT_trial.onset", t)
core.wait(0.5)

# start the experiment
for eachTrial,trigger in zip(HRE_trial, triggers):
    trigger.pop("Trial")
    eachTrial.pop("Trial")  # pop the unecessary info
    seq_list = list() # sequence list
    seq_num = 0 # cv counter
    mem_test_num = 0 # sequence counter
    cv_counter = 0 # cvs in a trial
    for key,value in eachTrial.items():
        # store the vlaue to the list
        seq_list.append(value)
        seq_num += 1
        # set sound and text for CVs
        HRE_audio.setSound(sound_file_prefix + str(value))
        HRE_txt.text = str(value[:-4])
        # play sound and show the CV text
        HRE_txt.draw()
        now = ptb.GetSecs()
        HRE_audio.play(when=now)

        # trigger onset
        if cv_counter % 9 == 0:
            exp_HRT.addData(trigger_key[cv_counter//9*2]+".EEGonset", trigger[trigger_key[cv_counter//9*2]])
            # ser.write(trigger[trigger_key[cv_counter//9*2]])

        win.flip()
        t = clock.getTime()
        exp_HRT.addData(key+".onset", t)
        # each stimuli last 500ms
        core.wait(0.5)
        # if counter reach 9 which mean a full sequence pass
        if seq_num == 9:
            # trigger offset
            exp_HRT.addData(trigger_key[cv_counter//9*2+1]+".EEGoffset", trigger[trigger_key[cv_counter//9*2+1]])
            # ser.write(trigger[trigger_key[cv_counter//9*2+1]])

            mem_test_num += 1
            # show a fixation for later memory test
            fixation.draw()
            win.flip()
            t = clock.getTime()
            exp_HRT.addData("HRT_Mem_test.fixation_"+str(mem_test_num)+".onset", t)
            core.wait(0.5)
            random.shuffle(seq_list) # this randomies the seq_list for memory test
            for index,text in enumerate(circles_txt):
                # the last one in the list is question mark so skip
                if index < 9:
                    # change the rest of the circle text to the item in the shuffled list
                    circles_txt[index].text = str(seq_list[index][:-4])
            list_resp = list()
            clicked_num = 0

            # the memory test at the end of the sequence
            win.mouseVisible = True
            t = clock.getTime()
            exp_HRT.addData("HRT_Mem_test_"+str(mem_test_num)+".onset", t)
            while True:
                for n, shape in enumerate(circles):
                    # when
                    if mouse.isPressedIn(shape):
                        clicked_num += 1
                        counter_txt.text = str(clicked_num) + "/9"
                        list_resp.append(circles_txt[n].text)
                        if circles_txt[n].text != '?':
                            del circles[n]
                            del circles_txt[n]
                        core.wait(0.1) # CAUTION: Do not click down mouse for too long, it will count as multiple clicks, can not be solved
                                       #          click time can only be within 100ms

                # if click respones more than 9 times, break out of the memory test
                if clicked_num == 9:
                    mouse.setPos(newPos=(700, -500))
                    break
                # change the text color when hover the text, give the participant an idea of which item they want to presss
                if circle_1.contains(mouse):
                    circle_1_txt.color = [-1,-1,-1]
                elif circle_2.contains(mouse):
                    circle_2_txt.color = [-1,-1,-1]
                elif circle_3.contains(mouse):
                    circle_3_txt.color = [-1,-1,-1]
                elif circle_4.contains(mouse):
                    circle_4_txt.color = [-1,-1,-1]
                elif circle_5.contains(mouse):
                    circle_5_txt.color = [-1,-1,-1]
                elif circle_6.contains(mouse):
                    circle_6_txt.color = [-1,-1,-1]
                elif circle_7.contains(mouse):
                    circle_7_txt.color = [-1,-1,-1]
                elif circle_8.contains(mouse):
                    circle_8_txt.color = [-1,-1,-1]
                elif circle_9.contains(mouse):
                    circle_9_txt.color = [-1,-1,-1]
                elif circle_question.contains(mouse):
                    circle_question_txt.color = [-1,-1,-1]

                # change back the color of the text when not hover
                else:
                    for index, text in enumerate(circles_txt):
                        circles_txt[index].color = [1,1,1]
             # drawing helps visual ize the mechanics
                for index, circle in enumerate(circles):
                    circles[index].draw()
                    circles_txt[index].draw()
                counter_txt.draw()
                win.flip()

            clicked_num = 0 # reset clicked number
            counter_txt.text = str(clicked_num) + "/9" # reset counter

            # reset circle and circle_text list
            circles = [circle_1, circle_2, circle_3, circle_4, circle_5,circle_6,circle_7,circle_8, circle_9, circle_question]
            circles_txt = [circle_1_txt, circle_2_txt, circle_3_txt, circle_4_txt, circle_5_txt,circle_6_txt,circle_7_txt,circle_8_txt, circle_9_txt, circle_question_txt]

            win.mouseVisible = False
            # show fixation point
            fixation.draw()
            win.flip()
            t = clock.getTime()
            exp_HRT.addData("HRT_Mem_test.end_fixation_"+str(mem_test_num)+".onset",t)
            core.wait(0.5)

            # print and save the response list
            exp_HRT.addData('practice.resp_'+str(mem_test_num), list_resp)

            seq_num = 0 # reset sequence counter
            seq_list = list() # reset sequence list for next list
        cv_counter += 1
    exp_HRT.nextEntry()

# store the end of the HRT trial
t = clock.getTime()
exp_HRT.addData("HRT_trial.offset", t)
# HRT experiment end screen
HRT_end_txt = visual.TextStim(win, pos=[0,0],height=80, text="The end of the first part of the experiment, press", units='pix')
HRT_end_txt.draw()
win.flip()

event.waitKeys()

# Rest session
rest_session_txt = visual.TextStim(win, pos=[0,50], height=50, text='Please take a rest')
countdown_timer = core.CountdownTimer(180)
countdown_min = "03"
countdown_sec = "00"
rest_countdown_txt = visual.TextStim(win, pos=[0,-50], height=80, text=countdown_min+":"+countdown_sec)
rest_countdown_txt.draw()
win.flip()
while countdown_timer.getTime() > 0:
    countdown_min = "0"+str(int(round(countdown_timer.getTime() // 60, 0)))
    if 60 > int(round(countdown_timer.getTime() % 60, 0)) >= 10:
        countdown_sec = str(int(round(countdown_timer.getTime() % 60, 0)))
    elif int(round(countdown_timer.getTime() % 60, 0)) == 60:
        countdown_sec = "00"
    else:
        countdown_sec = "0" + str(int(round(countdown_timer.getTime() % 60, 0)))
    rest_countdown_txt.text = countdown_min+":"+countdown_sec
    rest_session_txt.draw()
    rest_countdown_txt.draw()
    win.flip()

## <Serical recognition task>

# instruction screen
srt_instr = visual.TextStim(win, pos=[0,0], height=50, text='Serial recognition task')
srt_continue_txt = visual.TextStim(win, pos=[0,-500], height=30, text='<press space to continue>')
srt_continue_txt.draw()
srt_instr.draw()
win.flip()
event.waitKeys(keyList=['space'])

# prepare the HRE experiment lists
SRT_con_file = data.importConditions('Resource'+file_sep+'HRE_Experiment_Table.csv')
SRT_trial = data.TrialHandler(trialList=SRT_con_file, nReps=1, method = 'sequential')

# initialise component for SRT
SRT_txt = visual.TextStim(win, pos=[0,0], height=100, text='')
SRT_audio = sound.Sound(stereo=True)
# start fixation screen
fixation.draw()
win.flip()
t = clock.getTime()
exp_SRT.addData("SRT_trial.onset", t)
core.wait(0.5)

# start the Experiment
for eachTrial in SRT_trial:
    eachTrial.pop("Trial")  # pop the unecessary info
    seq_num = 0 # cv counter
    mem_test_num = 0
    cv_counter = 0 # cvs in a trial
    for key,value in eachTrial.items():
        seq_num += 1

        # trigger onset
        if cv_counter % 9 == 0:
            exp_SRT.addData(trigger_key[cv_counter//9*2]+".EEGonset", trigger[trigger_key[cv_counter//9*2]])
            # ser.write(trigger[trigger_key[cv_counter//9*2]])

        # set sound and text for CVs
        SRT_audio.setSound(sound_file_prefix + str(value))
        SRT_txt.text = str(value[:-4])
        # play sound and show the CV text
        SRT_txt.draw()
        now = ptb.GetSecs()
        SRT_audio.play(when=now)
        win.flip()
        t = clock.getTime()
        exp_SRT.addData(key+".onset", t)
        # each stimuli last 500ms
        core.wait(0.5)
        if seq_num == 9:
            mem_test_num += 1
            # show a fixation
            exp_SRT.addData(trigger_key[cv_counter//9*2+1]+".EEGoffset", trigger[trigger_key[cv_counter//9*2+1]])
            fixation.draw()
            win.flip()
            t = clock.getTime()
            exp_SRT.addData("SRT.fixation_"+str(mem_test_num)+".onset", t)
            core.wait(0.5)

            seq_num = 0 # reset sequence counter

        cv_counter += 1
    exp_SRT.nextEntry()
t = clock.getTime()
exp_SRT.addData("SRT.offset", t)

## end screen
end_txt = visual.TextStim(win, pos=[0,0],height=80 ,text='Thank you for participanting the experiment!', )
end_txt.wrapWidth = 1200
end_txt.draw()
win.flip()
event.waitKeys()


## Quit the Experiment
ser.close()
win.close()
core.quit()
