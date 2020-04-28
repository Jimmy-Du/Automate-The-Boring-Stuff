# Function:    commaList()
# Description: takes in a list of items that will be added into a string seperated by commas
# Parameters:  list: a list of items to be seperated by commas
# Return:      a string of containing the list items seperated with commas.
def commaList(list) :
    # checks to ensure that the list contains at least 1 item before seperating
    if len(list) != 0 :
        listToString = ''

        # for loop to 
        for i, item in enumerate(list) :
            # if the item is the last item in the list, the item is seperated by 'and'
                listToString += 'and ' + item
            # else, the item is seperated by a ','
            else :
                listToString += item + ', '

    return listToString



testList = ['dogs', 'cats', 'birds']

print(commaList(testList))
