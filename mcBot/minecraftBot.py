import pyautogui as pt
from time import sleep


# #helper function
# def nav_to_image(image, clicks, off_x=0, off_y=0):
#     position = pt.locateCenterOnScreen(image, confidence=.7)

#     if position is None:
#         print(f'{image} not found....')
#         return 0
#     else:
#         pt.moveTo(position, duration=.1)
#         pt.moveRel(off_x, off_y, duration=.1)
#         pt.click(clicks=clicks, interval=.3)

# def locate_lava():
#     position = pt.locateCenterOnScreen('mcBot/images/lava.png', confidence=.4)
#     position = pt.locateCenterOnScreen('mcBot/images/lavaFloor.png', confidence=.5)

#     if position is None:
#         return False
#     else:
#         #Move the charcter backwards if lava
#         move_character('s', 2)
#         print('Found Lava, running...')
#         return True
# def locate_water():
#     position = pt.locateCenterOnScreen('mcBot/images/water.png', confidence=.5)
#     position = pt.locateCenterOnScreen('mcBot/images/waterfloor.png', confidence=.5)

#     if position is None:
#         return False
#     else:
#         move_character('s', 2)
#         print('Found Water, running...')
#         return True

# #
# # Start the Game
# # sleep to allow time to tab over
# sleep(2)
# nav_to_image('mcBot/images/startButton.png', 3)


# # Moves the character
# # x = attack
# # c = place
def move_character(move_action, attack_action, effic, walk_length):
    pt.keyDown(move_action)
    sleep(walk_length)
    pt.keyUp(move_action)

    
    if attack_action == 'leftclick':
        pt.mouseDown(button='left')
        sleep(effic)
        pt.mouseUp()
        pt.move(0, 600)
        pt.mouseDown(button='left')
        sleep(effic)
        pt.mouseUp()
        pt.move(0, -600)

#-----MAIN----
sleep(2)
duration = 0
count = 0
while duration != 1500:
    stone_pick = 1.3
    iron_pick = 0.5
    diamond_pick = 0.4


    move_character('w', 'leftclick', stone_pick, 0.4)

    duration += 1
    #place torch
    if duration%20 == 0:
        pt.move(-500, -500)
        pt.click(button='right')
        pt.move(500,500)
        if count == 0:
            pt.keyDown('2')
            pt.keyUp('2')
        elif count == 1:
            pt.keyDown('3')
            pt.keyUp('3')
        elif count == 2:
            pt.keyDown('4')
            pt.keyUp('4')
            count = 0
            
        count +=1
    