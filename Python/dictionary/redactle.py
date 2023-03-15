import pyautogui as pt
from time import sleep
import pyperclip
#import json
import os


#        pt.keyDown('4')
#        pt.keyUp('4')
#        pt.click(button='right')
#        pt.move(500,500)
#        sleep(number)
#        pyperclip.copy('The text to be copied to the clipboard.')
#        spam = pyperclip.paste()

#copy paste function
def paste(word):
    pyperclip.copy(word)

    pt.keyDown('ctrl')
    pt.keyDown('v')
    pt.keyUp('v')
    pt.keyUp('ctrl') 
    pt.keyDown('enter')
    pt.keyUp('enter')

#-----MAIN----
#os.chdir("C:/Users/Jonty/GitHub/PersonalProjects/Python/dictionary")
# f = open(os.path.dirname(__file__)+"\\words.json")
# words = json.load(f)
f = open(os.path.dirname(__file__)+"\\freq.txt")
sleep(3)
pt.PAUSE = 0.00000000000000000000000001

for word in f:
    paste(word)







f.close()
