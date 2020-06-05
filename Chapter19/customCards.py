# File:        customCards.py
# Description: contains the createCustomCards function that reads in a file containing guests to create cards for, and
#              will generate a card for each guest



import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw



# constants to hold the flower image and font used for the card
kFlowerImage = 'flower.png'
kFontFile = 'FREESCPT.TTF'
# constants to hold the max width and height of the card
kMaxCardWidth = 288
kMaxCardHeight = 388
# constants to hold the max width and height of the border for the card
kCardWidthBorder = 287
kCardHeightBorder = 387



# Function:    createCustomCards()
# Description: goes through a file containing all guest names and creates a custom seating card for each of the
#              guests that contains their names
# Parameters:  guestFile: the file that contains the guest names to create cards for
# Return:      N/A
def createCustomCards(guestFile):
    fp = open(guestFile)
    guestList = fp.readlines()
    fp.close()

    # creates the folder to hold all the created cards
    os.makedirs('seatingCards', exist_ok=True)

    flowerImage = Image.open(kFlowerImage)

    # loop to go through all guest names in file and create custom seating cards for each guest
    for guest in guestList:
        # removes the newline character from the line containing the guest name
        guestName = guest[:-1]

        # creates a blank card, font used to print the guest name, and an ImageDraw object to draw on the card
        card = Image.new('RGBA', (kMaxCardWidth, kMaxCardHeight), 'white')
        cardFont = ImageFont.truetype(kFontFile, 24)
        cardDraw = ImageDraw.Draw(card)

        # pastes the flower image onto the card
        card.paste(flowerImage, (0,0))

        # adds border to the card
        cardDraw.line([(0, 0), (kCardWidthBorder, 0), (kCardWidthBorder, kCardHeightBorder), \
            (0, kCardHeightBorder), (0, 0)], fill='black')

        # adds the guest name onto the card
        cardDraw.text((120,100), guestName, fill='green', font=cardFont)

        card.save("seatingCards\%s_card.png" % (guestName))


        
createCustomCards('guests.txt')
