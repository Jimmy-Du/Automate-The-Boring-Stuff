import re



def regexStrip(argumentToStrip, charsToStrip):
    stripResult = ""

    # if no characters were specified to be stripped, trailing whitespace of the string will be stripped
    if charsToStrip == '':
        stripResult = argumentToStrip.strip()
    # else, the characters specified are stripped from the first string passed in
    else:
        removeRegex = re.compile(rf"[^{charsToStrip}]")
        stripResult = removeRegex.findall(argumentToStrip)
        stripResult = ''.join(stripResult)

    return stripResult



# prompt user for string to strip from and what chars to strip
userInput = input("Please enter a string to be stripped.\n")
charsToRemove = input("Please enter the characters to be stripped.*Optional*\n")

resultingString = regexStrip(userInput, charsToRemove)

print(resultingString)