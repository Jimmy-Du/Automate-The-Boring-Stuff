# File:        pdfPasswordBreaker.py
# Description: prompts user to enter the file path to the pdf to be brute forced, and cycles through all words in
#              the dictionary.txt file and attempts to decrypt the pdf until a match is found.



import os
import PyPDF2



# Function:    pdfPasswordBreaker()
# Description: goes through each word, both lowercase can uppercase variants,
#              found in dictionary.txt and attempts to decrypt the specified pdf file, if a match is found, the password is returned
# Parameters:  filePath: the file path to the pdf file to be decrypted
# Return:      the password that was able to successfully decrypt the passed in pdf file
def pdfPasswordBreaker(filePath):
    pdfFile = open(filePath, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFile)

    fp = open("dictionary.txt")
    passwords = fp.readlines()
    fp.close()

    correctPassword = ''

    # loop to go through all potential passwords in the file and attempt to decrypt the specified pdf file
    for password in passwords:
        password = password.strip()
        passwordLower = password.lower()
        passwordUpper = password.upper()

        # if the pdf is successfully decrypted using the current password, it is copied and the loop breaks
        if pdfReader.decrypt(password):
            correctPassword = password
            break
        # if the pdf is successfully decrypted using the current password in lowercase characters, it is 
        # copied and the loop breaks
        elif pdfReader.decrypt(passwordLower):
            correctPassword = passwordLower
            break
        # if the pdf is successfully decrypted using the current password in uppercase characters, it is 
        # copied and the loop breaks
        elif pdfReader.decrypt(passwordUpper):
            correctPassword = passwordUpper
            break
    
    return correctPassword



pdfFileInput = input("Please enter the file path to the pdf to brute force:\n")
password = pdfPasswordBreaker(pdfFileInput)

# if a password is returned, the password is printed
if password != '':
    print(f"Password is: {password}")
# else a message indicating that the password was not found
else:
    print("Password was not found")
