import time
from pynput import mouse, keyboard
import os
import pythonping as pyping

#-------------TO DO--------------
# 1. Rewrite the output file to where the K: line has the duration held on it as well [X]
# 2. Rewrite the output file to also contain the time between button presses - e.g. K:a 2.56 2.43 [X]
# 3. Make sure the packRunOutput file is made with multi threading for each button press, perhaps set a max num of threads,
#    so that each button isnt waiting on the sleep function of other buttons [X]

#-------------BUGS---------------
# 1. <RESOLVED> [DOUBLE REGISTER OF KEY] For example, holding 'w' and then holding 'd', followed by releasing 'w' will make 'd' register as being pressed again,
#  instead of merely maintaining the hold - leads to issue where 'd' is clicked again, causing a stutter in movement,
#  also causing the log to state 'K: d intervalTime1 durationTime1' and directly after, 'K: d intervalTime2 durationTime1' so that 
#  the duration time of it being held is the same, but the interval time between button presses is different
#
# 2. <RESOLVED> [Key Error When Deleting Times] - For example, hold 'w', click and release 'd', then click and release 'd' - do so in 
#  quick succession, and you get a key error. - this is due to previous bug fix for issue 1 --> setting heldDownKey = ""
#  caused a double click of a button to register it as a continuous hold, as the heldDownKey button was still equal to the same key
#  and so did not view it as a new button click, but as a hold. 
#
# 3. <WIP> [Special Keys do not work] need to troubleshoot allowing special keys such as Alt and Shift to work in this method


#-----------Mouse Inputs------------
def on_move(x, y):
    print('M:{0}'.format((x, y)))

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        print('C:left {0}{1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    elif button == mouse.Button.right:
        print('C:right {0}{1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    

def on_scroll(x, y, dx, dy):
    print('S:{0}{1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

#-----------Keyboard inputs---------
def on_press(key):
    global startTimeDict #keeps track of duration of key press & holds
    global heldKeyList #keeps track of all keys currently being held down
    global filePath
    global startBetweenTime #keeps track of duration between key presses
    global endBetweenTime #same as above^
    global serverIP

    try: #alphanumeric keys pressed
        if key.char not in heldKeyList: #if the key is being held, dont restart the time, or reprint it

            #----------ALL Time variables need to be executed as soon as possible---------
            endBetweenTime = time.time() #Get the time between the last time a button was pressed. The first time this occurs it is a very large number, ignore this - it will be handled in post
            betweenTime = endBetweenTime - startBetweenTime
            startBetweenTime = time.time() #start the clock for how long it has been since the last button press (needs to be placed)
            startTimeDict[key.char] = time.time() #append new start time as a key-value pair. 
            latency = pyping.ping(serverIP, count=1).rtt_avg_ms # retrieve server latency with one ping packet for how long it takes for the key to be registered as pressed    
            #-----------------------------------------------------------------------------

            #Write to file the key pressed and duration since last key press
            heldKeyList.append(key.char)  #saves the last key pressed to the list
            keyAndTime = 'K:{0}'.format(key.char) + ' ' + str(betweenTime) + ' ' + str(latency/1000) #using "K" to indicate a keyboard press
            print(keyAndTime) 
            file = open(filePath,"a") #append to file
            file.write(keyAndTime +'\n')
            file.close()
            
            
    
    except AttributeError: #special key pressed -------------NEEDS WORK--------------

        if '{0}'.format(key) not in heldKeyList:
            startTimeDict[key] = time.time() #append new start time as a key-value pair
            startBetweenTime = time.time()
            print('K:{0}'.format(key))
            heldKeyList.append('{0}'.format(key)) #saves the last key pressed to the list


def on_release(key):
    global startTimeDict
    global filePath
    global heldKeyList
    
    try: # this is done because if you dbl press a button, with any amount of time between, it will register as a continuous hold, so you need to reset
        heldKeyList.remove(key.char)
    except AttributeError:
        heldKeyList.remove(key)

    endTime = time.time() #get duration the key was pressed
    
    try: #alphanumeric key
        start = startTimeDict.get(key.char) #get the start time related to the key pressed and held from x amount of time ago
        del startTimeDict[key.char] #remove dictionary element to preserve uniquness of each key being pressed
    except AttributeError: #special key
        start = startTimeDict.get(key)
        del startTimeDict[key]
    
    try:         
        print('T:','{0}'.format(key.char), endTime - start) # What isnt obvious is that this accounts for releasing the shift key as well as 
                              # a regular key. For example, press Shift D, release D and then Shift.              
        file = open(filePath,"a")
        file.write('T:' + '{0}'.format(key.char) + ' ' + str(endTime - start) + '\n')
        file.close()
    except AttributeError: #special key pressed
        print('T:', '{0}'.format(key), endTime - start) # What isnt obvious is that this accounts for releasing the shift key as well as 
                              # a regular key. For example, press Shift D, release D and then Shift.
        file = open(filePath,"a")
        file.write('T:' + '{0}'.format(key) + ' ' + str(endTime - start) + '\n')
        file.close()
    
    if key == keyboard.Key.esc:
        # Stop listener
        #m_listener.stop()
        return False

def editText():
    
    file = open(filePath, 'r')
    Lines = file.readlines()
    file.close()
    finalText = []

    i = 0 #keep track of which line we are on
    for line in Lines:
        
        line = line.strip() # cotnains each individual line within the text File

        if line[0] == 'K': #check if a button press occured
            buttonP = line[2] #button to find

            for x in range(i, len(Lines)): #iterate through the Lines from our current position
                tempLine = Lines[x].strip() 
                print(tempLine)
                
                if tempLine[0] == 'T' and tempLine[2] == buttonP: #If a duration line was found, and its the same btn as btn we are searching for
                    duration = tempLine[tempLine.rindex(' ')+1:] #get the duration of time that the btn was held for
                    finalText.append(line + ' ' + duration) #edit the text value to include the duration held on one line
                    break #end the search 
        i += 1
        print(i)


    file = open(filePath, "w") #Finally, overwrite the old file with the new text
    for line in finalText:
        file.write(line + "\n")

    file.close()



#****************************************************MAIN*********************************************************

#----------Global Variables:--------------

k_listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
k_listener.start()

# m_listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)
# m_listener.start()


global fileName #each txt file will represent a complete run
fileName = "mahaToArcum.txt"
global filePath
filePath = os.path.join(os.path.dirname(__file__), fileName)
global startBetweenTime #Used to calculate the time between each button press
startBetweenTime = 0
global startTimeDict #keeps track of every start time by holding a key-value pair, 
                     #   where the key is the button pressed and the value is the time stamp
                     #   and this will remain unique via removing it once it's value is read. 
startTimeDict = {}
global heldKeyList #Keeps track of all concurrently held down keys. Each held key, once released, is removed from this list. 
heldKeyList = []
global serverIP #ServerIP to test latency between key presses when interacting across the internet
serverIP = "158.69.224.61"


#-----------Start Recording--------------
while k_listener.running:
    time.sleep(1)

#m_listener.stop()
k_listener.stop() #close the listeners

print("\n\n\n")
editText() #Reformat the outputted Text File




