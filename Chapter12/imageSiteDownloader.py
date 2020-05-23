# File:        imageSiteDownloader.py
# Description: prompts user for a search term and will then download all image search results from Imgur



import bs4
import requests
import os



# Function:    downloadImages()
# Description: takes a search term and downloads all image results from Imgur.
# Parameters:  search: the search term that images will be downloaded from
# Returns:     the number of images that were downloaded from the search term
def downloadImages(search):
    counter = 0

    # URLs for all image formats avaliable on Imgur
    jpgURL = "https://imgur.com/search/all?q_type=jpg&q_all=" + search

    # downloads the contents at the specified URL
    res = requests.get(jpgURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    imageElements = soup.select(".post > .image-list-link img")

    # creates a new directory with the search term to hold all image search results
    os.makedirs(f"{search} - Imgur", exist_ok=True)

    # loop that goes through all images retrieved and downloads them
    for image in imageElements:

        imageLink = "https:" + image.get('src')
        print("Downloading: " + imageLink)

        imageRequest = requests.get(imageLink)
        imageRequest.raise_for_status()

        imageFile = open(os.path.join(f"{search} - Imgur", os.path.basename(imageLink.replace('https://', ''))), 'wb')

        # loop that saves the current image to a file
        for chunk in imageRequest.iter_content(100000):
            imageFile.write(chunk)
    
        imageFile.close()

        counter += 1

    return counter



searchTerm = input("Please enter a term to search for:\n")
print(str(downloadImages(searchTerm)) + " images downloaded.")
