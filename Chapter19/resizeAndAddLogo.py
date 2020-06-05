# File:        resizeAndAddLogo.py 
# Description: Resizes all images in current working directory to fit 
#              in a 300x300 square, and adds catlogo.png to the lower-right corner.



import os
from PIL import Image



# constants to hold the logo picture file and the minimum size of the picture to avoid being resized
kSquareFitSize = 300
kLogoFilename = 'catlogo.png'



# Function:    resizeAndAdLogo()
# Description: goes through the specified directory and will resize and add logos to the image files found in 
#              the directory if the image is large enough.
# Parameters:  directory: the directory that contains the image files that will be resized and have logos added
# Return:      N/A
def resizeAndAddLogo(directory):
    logoIm = Image.open(kLogoFilename)
    logoWidth, logoHeight = logoIm.size

    os.makedirs('withLogo', exist_ok=True)
    # Loop over all files in the working directory.
    for filename in os.listdir(directory):
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.bmp') \
            or filename.lower().endswith('.gif')) or filename == kLogoFilename.lower():
            continue # skip non-image files and the logo file itself

        im = Image.open(filename)
        width, height = im.size

        # Check if image needs to be resized.
        if width > kSquareFitSize and height > kSquareFitSize:
            # Calculate the new width and height to resize to.
            if width > height:
                height = int((kSquareFitSize / width) * height)
                width = kSquareFitSize
            else:
                width = int((kSquareFitSize / height) * width)
                height = kSquareFitSize

            # Resize the image.
            print('Resizing %s...' % (filename))
            im = im.resize((width, height))

        # if the logo is too big for the image image, the logo will not be added
        if width < logoWidth * 2 and height < logoHeight * 2:
            print("Logo will not be added to image: %s as it is not big enough." % (filename))
        # else, the logo will be added to the current image
        else:
            print('Adding logo to %s...' % (filename))
            im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
            # Save changes.
            im.save(os.path.join('withLogo', filename))



resizeAndAddLogo('.')
