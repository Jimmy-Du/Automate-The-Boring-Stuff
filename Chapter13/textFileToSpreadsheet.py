# File:        textFileToSpreadsheet.py
# Description: prompts user to enter the directory path to the text files used to create the spreadsheet. Then will open each
#              text file in the directory and add the file contents into a spreadsheet file,  organized by having each file 
#              having its own column and each line within the file in a seperate row in the column.



import openpyxl
import os



# Function:     textFileToSpreadsheet()
# Desccription: gathers all text file contents from the specified directory and adds them into a spreadsheet. File contents are
#               organized by having each file having its own column and each line within the file in a seperate row in the column.
# Parameters:   directory: a string indicating the path to where the text file contents of the spreadsheet will be retrieved from
# Return:       N/A
def textFileToSpreadsheet(directory):
    # creates a new spreadsheet to hold the file contents in the specified directory
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Text File Contents"

    rowCounter = 1
    columnCounter = 1
    
    # loop to go through every file in the directory specified and determine if it is a text file
    for fileName in os.listdir(directory):
        # if the currently looked at file is a text file, its contents are read and added into the spreadsheet
        if fileName.endswith(".txt"):
            fp = open(fileName)
            fileContents = fp.readlines()
            fp.close()

            # loop to add each line from the previously opened file to the spreadsheet
            for line in fileContents:
                sheet.cell(row=rowCounter, column=columnCounter).value = line
                rowCounter += 1

            columnCounter += 1
            rowCounter = 1

    wb.save("textFileResults.xlsx")



directoryPrompt = input("Please enter the directory/folder path where the text files are located:\n")
textFileToSpreadsheet(directoryPrompt)
