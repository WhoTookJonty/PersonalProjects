import pyautogui as pt
from time import sleep
import os



#**********INSTRUCTIONS**************
#
#   Open StarRez
#   Click on the LUID of the first student on the roster verification list
#   Now run this script (you will have 8 seconds to do the next few instructions)
#   Press 'Entry' in the top left corner
#   Press 'Close' in the top left corner
#   This is all you have to do, now watch the script run. 
#
#*************************************

#function for keypresses
def keyPress(key, num): 
    for x in range(num):
        pt.keyDown(key)
        pt.keyUp(key)

#function to reduce duplication of enter keys
def enterKey():
    pt.keyDown('enter')
    pt.keyUp('enter')


#find image using pyautogui
def clickImage(img, found, off_x=0, off_y=0):
    found = False

    #loop until the image is found (as the website can take some time to load)
    while found == False:
        position = pt.locateCenterOnScreen(img, confidence=.9)

        if position is None:
            print(f'{img} not found....')
            found = False
        else:
            pt.moveTo(position, duration=.1)
            pt.moveRel(off_x, off_y, duration=.1)
            pt.click(clicks=1, interval=.3)
            found = True


#---------MAIN-----------
tabToNext = 2 #tab to next student
arrowDownToSelect = 2 #select 'In room' --> if you want to select any other option for every single student, just increase this number by 1 per item in the list
tabToSave = 1 #tab to save button after selecting 'In room'

numOfStudents = 29 #edit this according to the number of students needing roster verification

#countdown
for x in range(8):
    print(x, '...')
    sleep(1)



i = 1
found = False
while i <= numOfStudents:
    enterKey() #start process with the LUID highlighted
    sleep(1)

    #nav to roster verif 
    clickImage(os.path.dirname(__file__)+"\\images/rosterVerifButton.png", found)
    clickImage(os.path.dirname(__file__)+"\\images/editButton.png", found)
    sleep(1)

    #select 'In room'
    keyPress('down', arrowDownToSelect)
    keyPress('tab', tabToSave)
    enterKey()      

    #close back to main menu
    clickImage(os.path.dirname(__file__)+"\\images/entryButton.png", found)
    sleep(1)
    clickImage(os.path.dirname(__file__)+"\\images/closeButton.png", found)
    sleep(1)

    #select next student
    keyPress('tab', tabToNext)

    i += 1
print("")
print("***********Done!*************")


