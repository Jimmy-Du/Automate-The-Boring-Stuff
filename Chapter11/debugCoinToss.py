# File:        debugCoinToss.py
# Description: code provided in chapter 11 of Automate the Boring Things in Python to prompt user to guess heads or tails of
#              a coin flip, however, it contains bugs.
# Bugs fixed:  guess variable mistyped as "guesss"
#              toss variable is assigned a random number representing the coin flip, while the guess variable is assigned a
#              string by the user, and any comparisons between the 2 would fail.



import random



# constant dictionary to contain the valid coin flip options
kCoinSides = {0: "heads", 1: "tails"}

guess = ''

# loop that prompts the user to enter a side of a coin until they pick a valid option
while guess.tolower() != kCoinSides[0] and guess.tolower() != kCoinSides[1]:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = kCoinSides[random.randint(0, 1)] # 0 is heads, 1 is tails

# if the generated coin flip is the same as the user's guess, a winning message is displayed
if toss == guess:
    print('You got it!')
# else, the user is asked to guess again
else:
    print('Nope! Guess again!')
    guess = input()
    # if the user guessed the correct coin flip, a winning message is displayed
    if toss == guess:
        print('You got it!')
    # else, a losing message is displayed
    else:
        print('Nope. You are really bad at this game.')