def CommaList(list) :
    if len(list) != 0 :
        listToString = ''

        for i, item in enumerate(list) :
            if item == list[len(list) - 1] :
                listToString += 'and ' + item
            else :
                listToString += item + ', '

    return listToString


testList = ['dogs', 'cats', 'birds']

print(CommaList(testList))