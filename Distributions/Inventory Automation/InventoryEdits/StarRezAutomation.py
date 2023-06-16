import customtkinter as ctk
import pyautogui as pt
from time import sleep
import pyperclip
import os
import threading

#-------------Notes---------------- 
# can use pack, grid, or place to implement widgets


#----------------FUNCTIONS-----------------

#function for keypresses
def keyPress(key, num): 
    if thread_stop.is_set() == False:
        for x in range(num):
            pt.keyDown(key)
            pt.keyUp(key)

#function for enter key
def enterKey():
    if thread_stop.is_set() == False:
        pt.keyDown('enter')
        pt.keyUp('enter')

#paste function
def pasteValue(value):
    if thread_stop.is_set() == False:
        pyperclip.copy(value)
        pt.keyDown('ctrl')
        pt.keyDown('v')
        pt.keyUp('v')
        pt.keyUp('ctrl') 

#find image function
def clickImage(img):
        found = False
        #loop until the image is found (as the website can take some time to load)
        while found == False and thread_stop.is_set() == False:
            position = pt.locateCenterOnScreen(img, confidence=.80)

            if position is None:
                #print(f'{img} not found....')
                file = open(os.path.join(os.path.dirname(__file__), "log.txt"),"a")
                file.write(f'{img} not found...\n')
                file.close()
                found = False
            else:
                pt.moveTo(position, duration=.1)
                #pt.moveRel(off_x, off_y, duration=.1)
                pt.click(clicks=1, interval=.2)
                found = True

#navigation function to get to bulk edit in Recent Actions page
def nav_roomSpaceToBulkEdit():
    #navigation from roomSpace to BulkEdit
    if thread_stop.is_set() == False:
        clickImage(os.path.dirname(__file__)+"\\images\\roomSpaceActions.png")

        clickImage(os.path.dirname(__file__)+"\\images\\bulkEditInventories.png")
    
#navigation function from bulk edit to Criteria Selection
def nav_bulkEditToCriteriaSelection(itemToRemove):
    #nav to description and RecordType in Criteria Selection
    if thread_stop.is_set() == False:
        clickImage(os.path.dirname(__file__)+"\\images\\selectCriteria.png")
        
        clickImage(os.path.dirname(__file__)+"\\images\\searchCriteria.png")
        pasteValue("Description")
        
        clickImage(os.path.dirname(__file__)+"\\images\\description.png")
        
        clickImage(os.path.dirname(__file__)+"\\images\\empty.png")
        pasteValue(itemToRemove)

        clickImage(os.path.dirname(__file__)+"\\images\\saveCriteria.png")

        clickImage(os.path.dirname(__file__)+"\\images\\backButton.png")

        clickImage(os.path.dirname(__file__)+"\\images\\searchCriteria.png")
        pasteValue("Record Type")

        clickImage(os.path.dirname(__file__)+"\\images\\recordType.png")
        
        sleep(0.2)
        clickImage(os.path.dirname(__file__)+"\\images\\saveCriteria.png")
        
        clickImage(os.path.dirname(__file__)+"\\images\\close.png")
    

#---------------------DRIVER------------------
def add_run(arg):
    if thread_stop.is_set() == False:
        #------Item Variables------
        itemToRemove = item_entry.get()
        if num_items_entry.get() != '' and selection.get() != '':
            numOfItems = int(num_items_entry.get())
            editSetting = int(selection.get())

        #countdown
        sleep(3)

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

        clickImage(os.path.dirname(__file__)+"\\images/okButton.png") #Finalize changes
    

#------------------Thread Handling-----------

def create_thread():
    threadsActive = True
    global numThreads
    numThreads += 1
    t = threading.Thread(target=add_run, args=(numThreads, ), daemon=True)
    t.start()
    threadList.append(t)

def stop_threads():
    thread_stop.set()
    thread_stop.clear()
    threadsActive = False

def close_window():
    if threadsActive == True:
        stop_threads()
    root.destroy()
    

#Global Variables
thread_stop = threading.Event()
threadsActive = False
numThreads = 0
threadList = []
#-----------Overall Appearence--------------
ctk.set_appearance_mode("Dark")
root = ctk.CTk() #main widget (box that contains every other widget)
root.geometry("650x450") #window size, has to be called before mainloop
root.title("StarRez Delete Automation")


#-------------Widget Information-------------
#Title
title_label = ctk.CTkLabel(root, text="Enter Item Information", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=10)

#------Scrollable Frame---------
scrollable_frame = ctk.CTkScrollableFrame(root, width=550, height=300)
scrollable_frame.pack()

#Titles And Entry Fields
label = ctk.CTkLabel(scrollable_frame, text="Item Name", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(anchor="w")
item_entry = ctk.CTkEntry(scrollable_frame)
item_entry.pack(fill="x")

label = ctk.CTkLabel(scrollable_frame, text="Number of Items to Remove", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(pady=(15, 0), anchor="w")
num_items_entry = ctk.CTkEntry(scrollable_frame)
num_items_entry.pack(fill="x")

#Radio Buttons
label = ctk.CTkLabel(scrollable_frame, text="Edit Item to:", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(pady=(15, 0), anchor="w")

selection = ctk.StringVar() #need this to link all radiobuttons together
radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Deleted", value=1, font=ctk.CTkFont(size=15), variable=selection)
radiobutton.pack(pady=10, anchor="w")

radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Not Deletable Hidden", value=2, font=ctk.CTkFont(size=15), variable=selection)
radiobutton.pack(pady=(0, 10), anchor="w")

radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Not Deletable View", value=3, font=ctk.CTkFont(size=15), variable=selection)
radiobutton.pack(pady=(0, 10), anchor="w")

radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Not Deletable View Modify", value=4, font=ctk.CTkFont(size=15), variable=selection)
radiobutton.pack(pady=(0, 10), anchor="w")

#--------Run Action Button----------
#when "add_button is clicked, the add_run function is run."
add_button = ctk.CTkButton(root, text="Run", width=300, font=ctk.CTkFont(size=15, weight="bold"), command=create_thread) 
add_button.pack(pady=20)

def main():
    #------Start Application-------
    root.protocol("WM_DELETE_WINDOW", close_window)
    root.mainloop() #constantly running so long as the interface is running


if __name__ == "__main__":
    main()