import PySimpleGUI as psGUI
import os
from playsound import playsound, PlaysoundException
from random import shuffle

psGUI.theme('DarkTanBlue')
layout = [[psGUI.Text('Play music from ')], [psGUI.InputText()], [psGUI.Submit()]]
window = psGUI.Window('playSound', layout)
event, values = window.read()
window.close()

# player parameters
shuff = False
rep = False
wait = False
disp = False
try:
    if '?' in values[0]:
        values = values[0].split('?')
        if 'shuffle' in values:
            shuff = True
        if 'repeat' in values:
            rep = True
        if 'wait' in values:
            wait = True
        if 'list' in values:
            disp = True
except:
    raise SystemExit("player closed")

# base path
if values[0][:2] in ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:']:
    muse = values[0] + '/'
else:
    muse = os.path.join(os.path.expanduser("~"), "Desktop") + '/' + values[0] + '/'
muse = muse.replace('\\', '/')

# clear console
# windows
if os.name == 'nt':
    os.system('cls')
# linux, mac
else:
    os.system('clear')

# build playList
folderList = [muse]
playList = []
folderIndex = 0
folderDepth = 0
playsound('sfx/ice.mp3')
playsound('sfx/water.mp3')
print("Loading ... ", end='')
# psGUI.popup('Now Playing from ', muse)
playsound('sfx/forward.mp3')
for folder in folderList:
    folderDepth += 1
    for file in os.listdir(folder):
        if os.path.isfile(folder + file):
            if file[-4:] in [".mp3", ".wav"]:
                playList.append(folder + file)
        else:
            folderIndex += 1
            folderList.insert(folderIndex, folder + file + '/')
    folderIndex = folderDepth

# play sounds
fileLength = 0


def play(sound):
    global fileLength
    soundFile = sound.rsplit('/', 1)[1]
    print("\r\t" + " " * fileLength + "\r\t" + soundFile[:-4], end='')
    # psGUI.popup("Now Playing ... " + "\n\t" + soundFile[:-4])
    fileLength = len(soundFile) - 4
    try:
        playsound(sound)
    except PlaysoundException:
        playsound('sfx/alert.mp3')
        print("\r\t" + " " * fileLength + "\r\t" + " | bitrate too high | " + soundFile[:-4], end='')
        if not wait:
            input("")
    playsound('sfx/buffer.mp3')


# player
print("\r" + "Now Playing ... ")
while True:
    # player.shuffle
    if shuff:
        shuffle(playList)
    for s in playList:
        play(s)
        # player.wait
        if wait:
            playsound('sfx/bubblegum.mp3')
            input("")
        # player.list
        if disp:
            print("")
    # player.repeat
    if not rep:
        break
playsound('sfx/marbles.mp3')
