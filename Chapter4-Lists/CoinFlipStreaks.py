import random

numberOfStreaks = 0
numOfHeadsInRow = 0
numOfTailsInRow = 0

coinFlips = []

for experimentNumber in range(10000):
    # creates a list of 100 random 'heads' or 'tails' values.
    if random.randint(0,1) == 0:
        coinFlips.append('H')
        numOfHeadsInRow += 1
        numOfTailsInRow = 0
    else:
        coinFlips.append('T')
        numOfTailsInRow += 1
        numOfHeadsInRow = 0

    # checks if there is a streak of 6 heads or tails in a row.
    if numOfTailsInRow > 1 and numOfTailsInRow % 6 == 0 or numOfHeadsInRow % 6 == 0 and numOfHeadsInRow > 1:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))