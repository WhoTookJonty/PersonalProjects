import pyautogui as pt
import os
import time
import threading



def keyPress(key,duration, threadNum):
    with pt.hold(key):
        time.sleep(round(float(duration), 4))

def mouseMove(x, y):
    pt.move(x, y)


def mouseClick(btn):
    pt.click(button=btn)


def clickImage(img):
    position = pt.locateCenterOnScreen(img, confidence=.80)

    if position is None:
        #print(f'{img} not found....')
        file = open(os.path.join(os.path.dirname(__file__), "log.txt"),"a")
        file.write(f'{img} not found...\n')
        file.close()
    else:
        pt.moveTo(position, duration=.1)
        #pt.moveRel(off_x, off_y, duration=.1)
        pt.click(clicks=1, interval=.2)

def createThreads():
    global threadNum
    file = open(filePath, "r")
    Lines = file.readlines()

    time.sleep(3)

    for x in Lines:
        line = x.strip()

        if line[0] == 'K':
            line = line.replace('K:', '') #get rid of the Keypress indicator
            line = line.split(' ') #split by spaces, the element seperator
            print(list(line))
            time.sleep(round(float(line[1]), 4)) #wait after previous button press an x amount of time before pressing the next button
            t = threading.Thread(target=keyPress, args=(line[0],line[2], threadNum, ) ) # first element is the button, second element is the time to wait, third element is duration held
            t.start()
            threadList.append(t)
            threadNum += 1



global fileName
fileName = "mahaToArcum.txt"
global filePath 
filePath = os.path.join(os.path.dirname(__file__), fileName)
global threadNum
threadNum = 0
global threadList
threadList = []

time.sleep(3)

for x in range(10):
    print("-------------------START LOOP " + str(x) + "----------------")
    createThreads()


for thread in threadList:
    thread.join()


