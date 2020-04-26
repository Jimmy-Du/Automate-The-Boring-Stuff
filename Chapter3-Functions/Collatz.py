# File:        Collatz.py
# Date:        April 26, 2020
# Description: Asks user for an integer input and performs calculations on that number until the result is 1.



# Function:    collatz()
# Description: takes in a number divides it by 2 if the number is even, if the number is odd, it is multiplied by 3
#              and incremented by 1. The result of the calculation is returned.
# Parameters:  number: the number that the calculations will use
# Return:      the resulting number from the calculation
def collatz(number):
    # if the number is even, the number will be divided in half
    if number % 2 == 0 :
        return number / 2
    # else, the number is odd and will be multiplied by 3 and incremented by 1
    else:
        return 3 * number + 1



# try block that asks for an whole number input from the user
try:
    userNum = int(input('Please enter an integer value:\n'))
    
    # loop that performs the collatz calculation and prints the result until it results in 1
    while userNum != 1:
        userNum = int(collatz(userNum))
        print(userNum)

# if the user does not enter a whole number, an error message is displayed
except ValueError:
    print('Input was not an integer')
