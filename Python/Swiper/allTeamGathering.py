import pyautogui as pt
from time import sleep
import os


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

numOfStudents = 11 #edit this according to the number of students needing roster verification
numOfTimes = 6

#countdown
for x in range(8):
    print(x, '...')
    sleep(1)



i = 1
j = 1
found = False

while j <= numOfTimes:
    clickImage(os.path.dirname(__file__)+"\\images/selectAll.png", found)
    clickImage(os.path.dirname(__file__)+"\\images/swipeIn.png", found)

    while i <= numOfStudents:

        clickImage(os.path.dirname(__file__)+"\\images/groupStudentLeadershipGathering.png", found)

        i += 1
    j += 1
    i = 1
print("")
print("***********Done!*************")


