# File:        pdfDencrypt.py
# Description: prompts user for the directory path to encrypted pdf files and the password to decrypt them. Next, will then
#              go through each file in the directory and decrypt all encrypted pdf files with the supplied password and create
#              decrypted copies of the pdf.


import os
import PyPDF2



# Function:    decryptPDF()
# Description: goes through all pdf files in a specified directory and decrypts all encrypted files using the password specified
#              and saves a copy of the file ending with "_decrypted.pdf". 
# Parameters:  directory: the path to the directory that contains the encrypted pdf files to be decrypted
#              password: the password of the encrypted pdf files that are to be decrypted
# Return:      N/A
def decryptPDF(directory, password):
    # loop to go each file in the specified directory
    for filename in os.listdir(directory):
        # if the current file is a pdf file, the file will be opened for reading
        if filename.endswith(".pdf"):
            pdfFile = open(directory + "/" + filename, "rb")
            pdfReader = PyPDF2.PdfFileReader(pdfFile)

            # if the current pdf file is encrypted, an attempt to decrypt the file with the passed in password is made
            if pdfReader.isEncrypted == True:
                # if the pdf file is successfully decrypted, a decrypted copy will be created for the pdf
                if pdfReader.decrypt(password) == True:
                    pdfWriter = PyPDF2.PdfFileWriter()

                    # loop to add all pages of the pdf file into a new pdf file
                    for pageNum in range(pdfReader.getNumPages()):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))

                    # saves the newly decrypted pdf file
                    pdfResult = open(directory + "/" + filename[:-4] + "_decrypted.pdf", "wb")
                    pdfWriter.write(pdfResult)

                    pdfResult.close()

            pdfFile.close()



directoryInput = input("Please enter the directory to the PDF files to be decrypted:\n")
passwordInput = input("Please enter the password of the encrypted pdf files:\n")

decryptPDF(directoryInput, passwordInput)
