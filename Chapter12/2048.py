# File:        2048.py
# Description: opens up the firefox browser to the 2048 game and executes Up, Right, Down, Left pattern on the game.



from selenium import webdriver
from selenium.webdriver.common.keys import Keys



# Function:    play20480()
# Description: launches a firefox browser to the 2048 game url and constantly performs an Up, Right, Down, Left pattern
#              on the game
# Parameters:  N/A
# Return:      N/A
def play2048():
    # setup firefox to open to the 2048 game
    url = "https://play2048.co/"
    browser = webdriver.Firefox()
    browser.get(url)

    gameArea = browser.find_element_by_tag_name('html')


    # loop that constantly plays the Up, Right, Down, Left pattern on the 2048 game
    while True:
        gameArea.send_keys(Keys.UP)
        gameArea.send_keys(Keys.RIGHT)
        gameArea.send_keys(Keys.DOWN)
        gameArea.send_keys(Keys.LEFT)

        

play2048()
