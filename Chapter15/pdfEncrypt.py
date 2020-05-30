# File:        pdfEncrypt.py
# Description: prompts the user to enter the path to the directory containing pdf files to be encrypted and the password to
#              encrypt them with. Next, the program finds all pdf files and creates an encrypted copy of each pdf.



import os
import PyPDF2



# Function:    encryptPDF()
# Description: goes through all pdf files in the specified directory and creates encrypted copies with the password 
#              specified. All copies end with "_encrypted.pdf".
# Parameters:  directory: the path to the directory that contains pdf files to be encrypted
#              password: the password to be used to encrypt the pdf files in the directory
# Return:      N/A
def encryptPDF(directory, password):
    # loop to go through each file in the directory checking if it is a pdf file
    for filename in os.listdir(directory):
        # if the current file is a pdf file, it will be opened for reading
        if filename.endswith(".pdf"):
            pdfFile = open(directory + "/" + filename, "rb")
            pdfReader = PyPDF2.PdfFileReader(pdfFile)

            pdfWriter = PyPDF2.PdfFileWriter()

            # checks if the current pdf file is encrypted, if not, the contents of the pdf is copied into a new
            # pdf file
            if pdfReader.isEncrypted != True:
                # loop to copy the unencrypted pdf to the encrypted copy
                for pageNum in range(pdfReader.getNumPages()):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
            
            # encrypts the pdf file and saves it as a copy
            pdfWriter.encrypt(password)
            resultPdf = open(directory + "/" + filename[:-4] + "_encrypted.pdf", "wb")
            pdfWriter.write(resultPdf)

            pdfFile.close()
            resultPdf.close()



directoryInput = input("Please enter the directory to the PDF files to be encrypted:\n")
passwordInput = input("Please enter the password that the PDF files will be encrypted with:\n")

encryptPDF(directoryInput, passwordInput)
