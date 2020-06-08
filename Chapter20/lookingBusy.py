# File:        lookingBusy.py
# Description: constantly moves the cursor every 10 seconds to avoid looking idle on other applications



import pyautogui
import time



# constants to hold the amount of time between each cursor movement and the amount of pixels the cursor moves
kSecsPerMovement = 10
kCursorMovement = 5



# Function:    lookBusy()
# Description: constantly sleeps the program for 10 seconds and moves the cursor slightly every time it wakes up.
# Parameters:  N/A
# Return:      N/A
def lookBusy():
    print('Looking busy.\n Press Ctrl-C to stop.')

    try:
        # loop to move the cursor every 10 seconds
        while True:
            time.sleep(kSecsPerMovement)
            # moves cursor twice in opposite directions so that the cursor will stay in the same place
            pyautogui.move(kCursorMovement, 0)
            pyautogui.move(-kCursorMovement, 0)
    # if the user presses 'Ctrl-C' a message is printed indicating that the cursor movements have stopped
    except KeyboardInterrupt:
        print('Stopped looking busy.')



lookBusy()
