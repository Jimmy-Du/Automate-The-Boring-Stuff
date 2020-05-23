# File:        linkVerification.py
# Description: prompts user to enter a url, will then search for all links found at the URL and check if any lead to 404 
#              errors. Ends program after printing out the list of 404 error links.



import requests
import bs4



# Function:    verifyLinks()
# Description: searches for links on a specified URL, and checks if any of the links lead to a 404 error
# Parameters:  urlToVerify: the url of the page to verify that the links found on it are valid
# Returns:     a list of links that lead to a 404 error
def verifyLinks(urlToVerify):
    errorLinks = []

    res = requests.get(urlToVerify)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElements = soup.select("a")

    # loop to go through each link on the specified url, and checks if it leads to a 404 error
    for linkedLink in linkElements:
        
        # if the hyperlink tag contains an href property, it will be copied to be evaluated
        if linkedLink.get('href'):
            hrefLink = linkedLink['href']

            # if the href of the hyperlink tag starts with 'https://', the link will be requested
            if hrefLink.startswith('https://'):
                hrefRequest = requests.get(hrefLink)

                # if the request returns an 404 error code, it is added to a list containing all links that lead to errors
                if hrefRequest.status_code == 404:
                    errorLinks.append(hrefLink)

    return errorLinks
                    


url = input("Please enter a URL to verify links from:\n")
invalidLinks = verifyLinks(url)
print("404 Error Links:" + '\n'.join(invalidLinks))
