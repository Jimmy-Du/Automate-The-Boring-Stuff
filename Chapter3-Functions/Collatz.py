def collatz(number):
    if number % 2 == 0 :
        return number / 2
    else:
        return 3 * number + 1


try:
    userNum = int(input('Please enter an integer value:\n'))
    
    while userNum != 1:
        userNum = int(collatz(userNum))
        print(userNum)

except ValueError:
    print('Input was not an integer')