# File:        regexSearch.py
# Description: prompts the user for input of a regular expression, will then search the contents of all txt files and
#              print out any line in the files that contain a match with the regex provided by the user.



import re
from pathlib import Path



regexInput = input('Please enter a regular expression:\n')
userRegex = re.compile(rf'{regexInput}')

fileList = list(Path.cwd().glob('*.txt'))

fileContents = ''

# loop that gathers the contents of each file in the directory and loop for any matches with the regex
for file in fileList:
    directoryFile = open(file, 'r')
    fileContents = directoryFile.readlines()
    directoryFile.close()

    # loop to go through the current file contents and detect any matches with the regex
    for line in fileContents:
        # if there is a regex match in the current line, it is printed to the screen
        if userRegex.search(line) != None:
            print(line.strip('\n'))
