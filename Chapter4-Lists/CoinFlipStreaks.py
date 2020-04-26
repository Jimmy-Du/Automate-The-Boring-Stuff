import random



# counters to hold the number of streaks, number of head and tail coin flips in a row
numberOfStreaks = 0
numOfHeadsInRow = 0
numOfTailsInRow = 0

# list to hold the coin flip results
coinFlips = []

# creates a list of 10000 random 'heads' or 'tails' values.
for experimentNumber in range(10000):
    # if the randomly generated number is 0 indicating heads, an 'H' is appended to the list and
    # the counter of the heads in a row is incremented and the counter of tails in a row is reset to 0
    if random.randint(0,1) == 0:
        coinFlips.append('H')
        numOfHeadsInRow += 1
        numOfTailsInRow = 0
    # else, an 'T' is appended to the list and the counter of the tails in a row is incremented and the 
    # counter of heads in a row is reset to 0
    else:
        coinFlips.append('T')
        numOfTailsInRow += 1
        numOfHeadsInRow = 0

    # checks if there is a streak of 6 heads or tails in a row, and will increment the streak counter.
    if numOfTailsInRow > 1 and numOfTailsInRow % 6 == 0 or numOfHeadsInRow % 6 == 0 and numOfHeadsInRow > 1:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
