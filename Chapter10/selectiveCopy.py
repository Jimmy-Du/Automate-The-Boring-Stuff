# File:        selectiveCopy.py
# Description: prompts the user for a source folder to copy from, destination folder to copy to, and file extension
#              to look for to copy. Will then proceed to go through the source folder to find all files containing the
#              specified extension and copies them into the destination folder.



import re 
import os
import shutil



source = input("Please enter the folder path to copy from:\n")
destination = input("Please enter the folder path to paste to:\n")
extensionInput = input("Please enter a file extension to copy:\n")

# if the input for a file extension does not begin with a '.', it will be appended at the start of the extension
if extensionInput[0] != ".":
    extensionInput = "." + extensionInput

extensionRegex = re.compile(rf".*\{extensionInput}")

# loop that goes through each file in the source folder tree
for folderName, subfolders, fileNames in os.walk(source):
    # loop that goes through each file in the source folder tree and copies matching files with the inputted extension to 
    # the destination specified
    for fileName in fileNames:
        # if the current file contains the inputted file extension, it is then copied to the destination folder
        if extensionRegex.search(fileName) != None:
            shutil.copy(source + "\\" + fileName, destination)
