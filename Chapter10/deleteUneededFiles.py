# File:        deleteUneededFiles.py
# Description: Prompts user to enter the folder path to delete files from and what the minimum file size must be to delete.
#              Will then go through each file in the folder tree and list any files equal to or above the inputted user file
#              size.



import os
import pyinputplus as pyin



source = input("Please enter the folder path to delete from:\n")
fileSizeToDelete = pyin.inputInt("Please enter the minimum file size to be deleted in MB:\n")

print("Files to be deleted:")

# loop that goes through each file in the source folder tree
for folderName, subfolders, fileNames in os.walk(source):
    # loop that goes through each file in the file tree and checks if the file size is above the selected size and prints them
    for fileName in fileNames:
        fileSizeMB = os.path.getsize(folderName + "\\" + fileName) / 1000000
        # if the file currently evaluated is above the size indicated by the user, the absolute path is printed
        if fileSizeMB >= fileSizeToDelete:
            print(folderName + "\\" + fileName)
