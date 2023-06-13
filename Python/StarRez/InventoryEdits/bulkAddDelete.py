import pyautogui as pt
from time import sleep
import pyperclip
import os



#**********INSTRUCTIONS***************
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

#function for enter key
def enterKey():
    pt.keyDown('enter')
    pt.keyUp('enter')

def pasteValue(value):
    pyperclip.copy(value)
    pt.keyDown('ctrl')
    pt.keyDown('v')
    pt.keyUp('v')
    pt.keyUp('ctrl') 



#find image using pyautogui
def clickImage(img):
    found = False

    #loop until the image is found (as the website can take some time to load)
    while found == False:
        position = pt.locateCenterOnScreen(img, confidence=.80)

        if position is None:
            print(f'{img} not found....')
            found = False
        else:
            pt.moveTo(position, duration=.1)
            #pt.moveRel(off_x, off_y, duration=.1)
            pt.click(clicks=1, interval=.2)
            found = True
            
def nav_roomSpaceToBulkEdit():
    #navigation from roomSpace to BulkEdit
    clickImage(os.path.dirname(__file__)+"\\images/roomSpaceActions.png")

    clickImage(os.path.dirname(__file__)+"\\images/bulkEditInventories.png")
    

def nav_bulkEditToCriteriaSelection(itemToRemove):
    #nav to description and RecordType in Criteria Selection
    clickImage(os.path.dirname(__file__)+"\\images/selectCriteria.png")
    
    clickImage(os.path.dirname(__file__)+"\\images/searchCriteria.png")
    pasteValue("Description")
    
    clickImage(os.path.dirname(__file__)+"\\images/description.png")
    
    clickImage(os.path.dirname(__file__)+"\\images/empty.png")
    pasteValue(itemToRemove)

    clickImage(os.path.dirname(__file__)+"\\images/saveCriteria.png")

    clickImage(os.path.dirname(__file__)+"\\images/backButton.png")

    clickImage(os.path.dirname(__file__)+"\\images/searchCriteria.png")
    pasteValue("Record Type")

    clickImage(os.path.dirname(__file__)+"\\images/recordType.png")
    
    sleep(0.2)
    clickImage(os.path.dirname(__file__)+"\\images/saveCriteria.png")
    
    clickImage(os.path.dirname(__file__)+"\\images/close.png")
    

#--------------------------------MAIN---------------------------------


#------Item Variables------
itemToRemove = input("\nName of item (exactly as it appears in StarRez): ")
numOfItems = int(input("\nNumber of items to edit: ")) #edit this according to the number of items

#------Edit Settings--------
# editSetting = 1
# notDeletableHidden = 2
# notDeletableView = 3
# notDeletableViewModify = 4
print("Select what you want to edit the item to be: ")
print("1. Deleted")
print("2. Not Deletable Hidden")
print("3. Not Deletable View")
print("4. Not Deletable View Modify")
editSetting = int(input("\nEnter a number: "))



#countdown
for x in range(3):
    print(x, '...')
    sleep(1)


nav_roomSpaceToBulkEdit()
nav_bulkEditToCriteriaSelection(itemToRemove)


#Remove the selected item in bulk edit
i = 1
clickImage(os.path.dirname(__file__)+"\\images/editInventoryView.png") #loop until the viewport shows up (avoids bug of clicking wrong img)
while i <= numOfItems:

    clickImage(os.path.dirname(__file__)+"\\images/normalSetting.png")
    keyPress("down", editSetting)
    enterKey()

    i += 1


print("")
clickImage(os.path.dirname(__file__)+"\\images/okButton.png") #Finalize changes

print("***********Done!*************")


