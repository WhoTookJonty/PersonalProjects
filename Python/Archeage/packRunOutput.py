import pyautogui as pt
import os
import time
import threading
import pythonping as pyping

#-----------NOTES---------
# There appears to be a general network delay, causing me to have to increase the time to hold and time to wait to account


def keyPress(key, latency, duration, threadNum):
    global serverIP
    global currLatency
    start = time.time()
    currLatency = (pyping.ping(serverIP, count=1).rtt_avg_ms)/1000
    duration = float(duration) + float(latency)/1000 + (float(currLatency) - float(latency)) # add the past latency first because you held a key for that length of time originally, 
                                                                        # then account for the new latency by getting the difference between the two, and adding that. 
                                                                        # if the difference is negative: the current latency is lower & we need to minus the extra time
                                                                        # if the difference is positive: the current latency is higher and we need to add on extra time
    with pt.hold(key):
        while time.time() - start < float(duration):
            time.sleep((float(duration) - (time.time()-start))+currLatency*3 + 0.01) # sleep for just slightly less than the time to get to ensure accuracy of timing, 
                                                                # and it also means the while loop will not constantly have to loop in order to keep track of time. 

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


def createThreads(keyList):
    global threadNum
    global currLatency
    currLatency = 0 # init to zero
    i = 0
    while i < len(keyList):
        
        
        wait = float(keyList[i+1]) # retrieve the duration between each button press
        start = time.time() # start the timer for the wait function
        while time.time() - start < wait:
            time.sleep((wait - (time.time()-start))) # sleep for just slightly less than the time to get to ensure accuracy of timing, 
                                                     # and it also means the while loop will not constantly have to loop in order to keep track of time. 
       
        #Note: i = key pressed, i+1 = wait time, i+2 = latency, i+3 = duration key is held for
        t = threading.Thread(target=keyPress, args=(keyList[i], keyList[i+2], keyList[i+3], threadNum, ) ) # execute a thread per button pressed
        t.start()
        threadList.append(t)
        threadNum += 1
        i += 4 # number of variables being passed in from the text file
        



global fileName #this holds all of the keylogging data
fileName = "mahaToArcum.txt"
global filePath 
filePath = os.path.join(os.path.dirname(__file__), fileName)
global threadNum # keeps count of the total number of threads (also ensures unique creation of threads)
threadNum = 0
global threadList #holds all the unique threads created
threadList = []
global serverIP
serverIP = "158.69.224.61" #used to detect latency to the server to account for difference in time of key presses


time.sleep(3)
keyList = []

for x in range(1):
    print("-------------------START LOOP " + str(x) + "----------------")
    
    file = open(filePath, "r")
    Lines = file.readlines()
    
    for x in Lines:
        line = x.strip()

        if line[0] == 'K':
            line = line.replace('K:', '') #get rid of the Keypress indicator
            line = line.split(' ') #split by spaces, the element seperator
            print(list(line))
            keyList.append(line[0]) # key pressed
            keyList.append(line[1]) # time since last key press (i.e. the 'wait' time)
            keyList.append(line[2]) # latency of the server
            keyList.append(line[3]) # duration the key is held for
            
    createThreads(keyList)


for thread in threadList:
    thread.join()


