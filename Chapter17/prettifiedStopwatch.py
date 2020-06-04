# File:        prettifiedStopwatch.py
# Description: waits for user input to start the stopwatch, every input afterwards displays the lap and total time to
#              the user. A Ctrl-C input will cause the stopwatch to stop completely and save the contents to the clipboard.



import time
import pyperclip



# Function:    stopwatch()
# Description: waits for user input to start the stopwatch, every input afterwards displays the lap and total time to
#              the user. A Ctrl-C input will cause the stopwatch to stop completely and save the contents to the clipboard.
# Parameters:  N/A
# Return:      N/A
def stopwatch():
    # Display the program's instructions.
    print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
    input()                    # press Enter to begin
    print('Started.')

    startTime = time.time()    # get the first lap's start time
    lastTime = startTime
    lapNum = 1

    clipboard = ""

    # Start tracking the lap times.
    try:
        # loop that waits for user input and displays the current stopwatch lap and total times
        while True:
            input()
            # calculates the lap and total times
            lapTime = round(time.time() - lastTime, 2)
            totalTime = round(time.time() - startTime, 2)
            # formats the lap info and prints to screen
            lap = 'Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).center(5), str(lapTime).rjust(6))
            print(lap, end='')
            clipboard += lap + "\n"
            lapNum += 1
            lastTime = time.time() # reset the last lap time
    # Handle the Ctrl-C exception to keep its error message from displaying.
    except KeyboardInterrupt:
        print('\nDone.')
        print("Results copied to clipboard.")
        pyperclip.copy(clipboard)



stopwatch()
