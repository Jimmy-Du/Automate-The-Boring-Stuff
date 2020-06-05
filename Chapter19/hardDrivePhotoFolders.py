# File:        hardDrivePhotoFolders.py
# Description: goes through every folder on the hard drive and prints out the absolute paths of any folder that is considered
#              a photo folder. A photo folder is defined as a folder with half its files being image files and the width and
#              height of the photo are 500 or more pixels.



import os
from PIL import Image



kMinPhotoSize = 500



# loop to go through each folder and file on the hard drive
for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if filename.lower().endswith('.png') != True and filename.lower().endswith('jpg') != True:
            numNonPhotoFiles += 1
            continue    # skip to next filename

        im = Image.open(os.path.join(foldername, filename))
        width, height = im.size

        # Check if width & height are larger than 500.
        if width < kMinPhotoSize or height < kMinPhotoSize:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos, it will display the absolute path of the folder.
    if numPhotoFiles > numPhotoFiles:
        print(os.path.abspath(foldername))
