# File:        instantMessengerBot.py
# Description: automatically sends a message through Microsoft Teams to a specified contact



import time
import pyautogui



# Function:    sendTeamsMessage()
# Description: automatically sends a Microsoft Teams message to the specified contact 
# Parameters:  contact: a string containing the username of the contact to message
#              message: a string containing the message to send to the contact
# Return:      N/A
def sendTeamsMessage(contact, message):
    # alerts and waits for user to switch to the Microsoft Teams window
    print('Please switch to the Microsoft Teams application/window.')
    print('Starting in ', end=''); pyautogui.countdown(5)
    
    # performs shortcut to the search bar and enters the contact to search for
    pyautogui.hotkey('ctrl', 'e')
    pyautogui.write(contact)

    # put program to sleep for one second to allow search results to display
    time.sleep(1)

    pyautogui.press('down')
    pyautogui.press('enter')

    # put program to sleep for one second to allow chat to display
    time.sleep(1)

    # writes and sends message
    pyautogui.write(message)
    pyautogui.press('enter')



contactInput = input('Please enter the username of the person to send the message to:\n')
messageInput = input('Please enter the message to send:\n')

sendTeamsMessage(contactInput, messageInput)
