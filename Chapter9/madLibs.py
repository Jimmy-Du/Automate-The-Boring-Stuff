# File:        madLibs.py
# Description: opens a file and searches for occurences of madlib keywords and prompts the user
#              to fill out the keyword, will then replace the keyword with their input and save the
#              results to a new file.



import re



madLibRegex = re.compile(r'ADJECTIVE|NOUN|VERB')

madLibFile = open('madLibs.txt', 'r')
madLibContents = madLibFile.read()
madLibFile.close()

# loop that finds each keyword in the madlibs file and prompts user their replacement
while madLibRegex.search(madLibContents) != None:
    request = madLibRegex.search(madLibContents).group()
    replacement = input(f"Please enter a {request.lower()}:\n")
    madLibContents = madLibContents.replace(request, replacement, 1)

# creates a new file and save the filled out mad lib into it
madLibResultFile = open('madLibsResult.txt', 'w')
madLibResultFile.write(madLibContents)
madLibResultFile.close()

print(madLibContents)
    