from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service # Used to remove the Command Prompt Window on desktop app
import threading
from time import sleep
import customtkinter as ctk


#-------------Distribution Notes---------------- 
# pyinstaller --noconfirm --onefile --windowed --add-data "c:\users\jonty\appdata\local\programs\python\python310\lib\site-packages/customtkinter;customtkinter/"  StarRezSelenium.py


#===============FUNCTIONS============


# -----POPUP WINDOWS-----
def displayErrorWin(localThreadNum, text):
    if all_threads_stop.is_set() == False:
        win = ctk.CTkToplevel(root)
        x = root.winfo_x()
        y = root.winfo_y()
        win.geometry("+%d+%d" %(x+200,y+200))
        win.title("Information")
        win.wm_transient(root)

        popup_label = ctk.CTkLabel(win, text=text, font=ctk.CTkFont(size=20, weight="bold"))
        popup_label.pack(padx=10, pady=20)
        ok_button = ctk.CTkButton(win, text="OK", width=100, font=ctk.CTkFont(size=15, weight="bold"), command=win.destroy) 
        ok_button.pack(pady=10)
        
        if localThreadNum != -1:
            stopThread(localThreadNum)
            driverList[localThreadNum].quit() #close out the driver window
    

def displayOkWin(localThreadNum):
    top = ctk.CTkToplevel(root)
    x = root.winfo_x()
    y = root.winfo_y()
    top.geometry("+%d+%d" %(x+200,y+200))
    top.title("Information")
    top.wm_transient(root)

    popup_label = ctk.CTkLabel(top, text="All Done!", font=ctk.CTkFont(size=20, weight="bold"))
    popup_label.pack(padx=10, pady=20)
    ok_button = ctk.CTkButton(top, text="OK", width=100, font=ctk.CTkFont(size=15, weight="bold"), command=top.destroy) 
    ok_button.pack(pady=10)

    stopThread(localThreadNum)
    driverList[localThreadNum].quit() #close out the driver window


# -------ELEMENT FINDING---------
def waitForElement(xPath, handleError, localThreadNum):
    if all_threads_stop.is_set() == False and threadEventList[localThreadNum].is_set() == False:
        try:
            WebDriverWait(driverList[localThreadNum], 10).until(EC.presence_of_element_located((By.XPATH, xPath)))
        except TimeoutException:
            print("Loading took too much time")
            if handleError == True:
                displayErrorWin(localThreadNum, "Page Took Too Long...")
            return -1

def findElement(xPath, handleError, localThreadNum):
    if all_threads_stop.is_set() == False and threadEventList[localThreadNum].is_set() == False:
        try:
            return WebDriverWait(driverList[localThreadNum], 10).until(EC.presence_of_element_located((By.XPATH, xPath)))
        except TimeoutException:
            print("Loading took too much time")
            if handleError == True:
                displayErrorWin(localThreadNum, "Page Took Too Long...")
            return -1

def findAndClick(xPath, handleError, localThreadNum):
    if all_threads_stop.is_set() == False and threadEventList[localThreadNum].is_set() == False:
        try:
            WebDriverWait(driverList[localThreadNum], 10).until(EC.presence_of_element_located((By.XPATH, xPath))).click()
        except TimeoutException:
            print("Loading took too much time")
            if handleError == True:
                displayErrorWin(localThreadNum, "Page Took Too Long...")
            return -1


def findAndSendKeys(xPath, keys, handleError, localThreadNum):
    if all_threads_stop.is_set() == False and threadEventList[localThreadNum].is_set() == False:
        try:
            WebDriverWait(driverList[localThreadNum], 10).until(EC.presence_of_element_located((By.XPATH, xPath))).send_keys(keys)
        except TimeoutException:
            print("Loading took too much time")
            if handleError == True:
                displayErrorWin(localThreadNum, "Page Took Too Long...")
            return -1

def selectOption(editOption, quantity, xPath, handleError, localThreadNum):
    if all_threads_stop.is_set() == False and threadEventList[localThreadNum].is_set() == False:

        try:
            WebDriverWait(driverList[localThreadNum], 10).until(EC.presence_of_element_located((By.XPATH, xPath)))
            selectArr = driverList[localThreadNum].find_elements(By.XPATH, xPath)
        except TimeoutException:
            print("Loading took too much time")
            if handleError == True:
                displayErrorWin(localThreadNum, "Page Took Too Long...")
            return -1
        
        for i in range(quantity):
            select = Select(selectArr[i])
            select.select_by_value(editOption)


# -----NAVIGATION-----
def navigate_ToRoomSpace(roomSpace, localThreadNum):
    if all_threads_stop.is_set() == False and threadEventList[localThreadNum].is_set() == False:
    
        findAndClick('//button[@class="ui-redirect-providers sr_button_primary sr_button"]', True, localThreadNum)

        
        while  findAndClick('//div[@class="icon-rooms icon"]', False, localThreadNum) == -1: #Wait indefinitely until the user has logged in
            ""

        findAndSendKeys('//div[@class="grid-filter-controls "]//input[@class="fill ui-dont-track ui-input"]', roomSpace, True, localThreadNum) #the space after "controls" is vital to finding this element.

        findAndClick(f'//a[@class="ui-open-detailscreen"][text()="{roomSpace}"]', True, localThreadNum)
        findAndClick('//a[@class="multiple"][contains(text(), "Inventory Items")]', True, localThreadNum)



def bulk_EditInventory(item, currentItemType, localThreadNum):
    if all_threads_stop.is_set() == False and threadEventList[localThreadNum].is_set() == False:
        findAndClick('//button[@title="Room Space Actions"]', True, localThreadNum) # Go to roomspace actions
        findAndClick('//a[@data-groupkey="Inventory"]', True, localThreadNum) #Select Inventory
        findAndClick('//ul//li//a[contains(text(), "Bulk Edit Inventories")]', True, localThreadNum) # Select bulk edit
        findAndClick('//div[@class="contents-static-buttons ui-contents-static-buttons"]//button[@aria-label="Select Criteria (0)"]', True, localThreadNum) # Select the Select Criteria option to filter results
        findAndClick('//label[@title="Description"]', True, localThreadNum) # Select Description
        findAndSendKeys('//input[@class="large ui-dont-track ui-input"][@name="Description"]', item, True, localThreadNum) #Set it to the item to edit
        findAndClick('//button[@aria-label="Save Criteria"]', True, localThreadNum) # Save this entry
        findAndClick('//label[@title="Record Type"]', True, localThreadNum) # Select the Record Type
        selectOption(currentItemType, 1, '//select[@name="RecordTypeEnum"][@class="ui-dont-track ui-input"]', True, localThreadNum)
        findAndClick('//button[@aria-label="Save Criteria"]', True, localThreadNum) # If you want to keep the Record Type as Normal just save right away SUBJECT TO CHANGE
        findAndClick('//button[@aria-label="Close"]', True, localThreadNum) # Close the criteria page

        #ensures that the filtered records are displayed before any further action
        waitForElement('//div[@class="info data-message ui-data-message"][contains(text(), "Filtered")]', True, localThreadNum) 

        
#----Thread Handling----

def createThread():
    if num_items_entry.get() != '' and selectionTwo.get() != '' and selectionOne.get() != '' and item_entry.get() != '' and room_entry.get() != '':
        global numThreads
        numThreads += 1
        
        chrome_service = Service() #not setting an executable path will default it to using chromedriver
        chrome_service.creation_flags = 0x08000000 #this flag prevents a command prompt from opening when using the desktop app
        driver = webdriver.Chrome(service=chrome_service)
        driverList.append(driver) # appending driver instances to allowing a driver to be run for each thread
        
        thread_stop = threading.Event()
        threadEventList.append(thread_stop)

        t = threading.Thread(target=addRun, args=(numThreads, ), daemon=True)
        t.start()
        threadList.append(t)

        print("---------------Starting ThreadList------------")
        print("Number of threads = ", numThreads)
        print()
        print(threadList)
        print()
    else:
        displayErrorWin(-1, "Please Fill Out All Fields")

def shutDownProgram():
    all_threads_stop.set()
   

    print("---------------Stopped ThreadList------------")
    print("Number of threads = ", numThreads)
    print()
    print(threadList)
    print()
    print("**********************************************")

    for x in driverList:
        x.quit()
    root.destroy()



def stopThread(localThreadNum):
    threadEventList[localThreadNum].set()

    print("---------------Stopped ThreadList------------")
    print("Number of threads = ", numThreads)
    print()
    print(threadList)
    print()
    print("**********************************************")


#---------DRIVER---------

def addRun(localThreadNum):
    if all_threads_stop.is_set() == False and threadEventList[localThreadNum].is_set() == False: #ensure threads are allowed to keep running
        
        #------Item Variables------
        quantity = int(num_items_entry.get())
        editOption = selectionTwo.get()
        currentItemType = selectionOne.get()
        item = item_entry.get()
        roomSpace = room_entry.get()
        driverList[localThreadNum].get("https://liberty.starrezhousing.com/StarRezWeb/dashboard/1720")

        try:
            navigate_ToRoomSpace(roomSpace, localThreadNum)

            bulk_EditInventory(item, currentItemType, localThreadNum)

            selectOption(editOption, quantity, '//select[@name="RoomSpaceInventory.RecordTypeEnum"]', True, localThreadNum)

            findAndClick('//div[@class="ui-wizard-buttons"]//button[@class="ui-btn-ok sr_button_primary sr_button"]', True, localThreadNum)
            
            displayOkWin(localThreadNum)
        
        except: 
            displayErrorWin(localThreadNum, "Something Went Wrong...")
            return -1
        


#--------------Global Variables--------------
all_threads_stop = threading.Event()
numThreads = -1
threadList = []
driverList = []
threadEventList = []


#Overall Appearence
ctk.set_appearance_mode("Dark")
root = ctk.CTk() #main widget (box that contains every other widget)

h = 650
w = 450

ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.geometry("650x450") #window size, has to be called before mainloop
root.title("StarRez Automation")


#Widget Information
#Title
title_label = ctk.CTkLabel(root, text="Enter Item Information", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=10)

#Scrollable Frame
scrollable_frame = ctk.CTkScrollableFrame(root, width=550, height=300)
scrollable_frame.pack()

#Titles And Entry Fields
label = ctk.CTkLabel(scrollable_frame, text="Room Space", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(anchor="w")
room_entry = ctk.CTkEntry(scrollable_frame)
room_entry.pack(fill="x")

label = ctk.CTkLabel(scrollable_frame, text="Item Name", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(pady=(15, 0), anchor="w")
item_entry = ctk.CTkEntry(scrollable_frame)
item_entry.pack(fill="x")

label = ctk.CTkLabel(scrollable_frame, text="Number of Items", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(pady=(15, 0), anchor="w")
num_items_entry = ctk.CTkEntry(scrollable_frame)
num_items_entry.pack(fill="x")

#Radio Buttons for Current Item
label = ctk.CTkLabel(scrollable_frame, text="Current Item Record Type:", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(pady=(15, 0), anchor="w")

selectionOne = ctk.StringVar() #need this to link all radiobuttons together
radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Normal", value=0, font=ctk.CTkFont(size=15), variable=selectionOne)
radiobutton.pack(pady=(10, 0), anchor="w")

radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Deleted", value=1, font=ctk.CTkFont(size=15), variable=selectionOne)
radiobutton.pack(pady=10, anchor="w")

radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Not Deletable Hidden", value=2, font=ctk.CTkFont(size=15), variable=selectionOne)
radiobutton.pack(pady=(0, 10), anchor="w")

radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Not Deletable View", value=3, font=ctk.CTkFont(size=15), variable=selectionOne)
radiobutton.pack(pady=(0, 10), anchor="w")

radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Not Deletable View Modify", value=4, font=ctk.CTkFont(size=15), variable=selectionOne)
radiobutton.pack(pady=(0, 10), anchor="w")

#Radio Buttons For Editing
label = ctk.CTkLabel(scrollable_frame, text="Edit Item to:", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(pady=(15, 0), anchor="w")

selectionTwo = ctk.StringVar() #need this to link all radiobuttons together
radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Normal", value=0, font=ctk.CTkFont(size=15), variable=selectionTwo)
radiobutton.pack(pady=(10, 0), anchor="w")

radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Deleted", value=1, font=ctk.CTkFont(size=15), variable=selectionTwo)
radiobutton.pack(pady=10, anchor="w")

radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Not Deletable Hidden", value=2, font=ctk.CTkFont(size=15), variable=selectionTwo)
radiobutton.pack(pady=(0, 10), anchor="w")

radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Not Deletable View", value=3, font=ctk.CTkFont(size=15), variable=selectionTwo)
radiobutton.pack(pady=(0, 10), anchor="w")

radiobutton = ctk.CTkRadioButton(scrollable_frame, text="Not Deletable View Modify", value=4, font=ctk.CTkFont(size=15), variable=selectionTwo)
radiobutton.pack(pady=(0, 10), anchor="w")

#Run Action Button
#when "run_button is clicked, the addRun function is run."
run_button = ctk.CTkButton(root, text="Run", width=300, font=ctk.CTkFont(size=15, weight="bold"), command=createThread) 
run_button.pack(pady=20)



def main():
    #Start Application
    root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())
    root.mainloop() #constantly running so long as the interface is running


if __name__ == "__main__":
    main()