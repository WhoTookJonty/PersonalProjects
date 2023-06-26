from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time


def waitForElement(text):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, text)))
    except TimeoutException:
        print("Loading took too much time")

def findElement(text):
    try:
        return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, text)))
    except TimeoutException:
        print("Loading took too much time")

def findAndClick(text):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, text))).click()
    except TimeoutException:
        print("Loading took too much time")


def findAndSendKeys(text, keys):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, text))).send_keys(keys)
        except TimeoutException:
            print("Loading took too much time")

def selectOption(editOption, quantity):
    selectArr = driver.find_elements(By.XPATH, '//select[@name="RoomSpaceInventory.RecordTypeEnum"]')

    for i in range(quantity):
        select = Select(selectArr[i])
        select.select_by_value(editOption)


def navigate_ToRoomSpace(roomSpace):
    
    findAndClick('//button[@class="ui-redirect-providers sr_button_primary sr_button"]')

    i = 1
    while i < 20:
        print(i)
        time.sleep(1)
        i = i+1

    findAndClick('//div[@class="icon-rooms icon"]')

    findAndSendKeys('//div[@class="grid-filter-controls "]//input[@class="fill ui-dont-track ui-input"]', roomSpace) #the space after "controls" is vital to finding this element.

    findAndClick(f'//a[@class="ui-open-detailscreen"][text()="{roomSpace}"]')
    findAndClick('//a[@class="multiple"][contains(text(), "Inventory Items")]')



def bulk_EditInventory(item):
    findAndClick('//button[@title="Room Space Actions"]') # Go to roomspace actions
    findAndClick('//a[@data-groupkey="Inventory"]') #Select Inventory
    findAndClick('//ul//li//a[contains(text(), "Bulk Edit Inventories")]') # Select bulk edit
    findAndClick('//div[@class="contents-static-buttons ui-contents-static-buttons"]//button[@aria-label="Select Criteria (0)"]') # Select the Select Criteria option to filter results
    findAndClick('//label[@title="Description"]') # Select Description
    findAndSendKeys('//input[@class="large ui-dont-track ui-input"][@name="Description"]', item) #Set it to the item to edit
    findAndClick('//button[@aria-label="Save Criteria"]') # Save this entry
    findAndClick('//label[@title="Record Type"]') # Select the Record Type
    findAndClick('//button[@aria-label="Save Criteria"]') # If you want to keep the Record Type as Normal just save right away SUBJECT TO CHANGE
    findAndClick('//button[@aria-label="Close"]') # Close the criteria page

    #ensures that the filtered records are displayed before any further action
    waitForElement('//div[@class="info data-message ui-data-message"][contains(text(), "Filtered")]') 




driver = webdriver.Chrome()

driver.get("https://liberty.starrezhousing.com/StarRezWeb/dashboard/1720")

navigate_ToRoomSpace("001-A853")

bulk_EditInventory("Light")

selectOption("1", 4)

time.sleep(3)

findAndClick('//div[@class="ui-wizard-buttons"]//button[@class="ui-btn-ok sr_button_primary sr_button"]')

time.sleep(6)

