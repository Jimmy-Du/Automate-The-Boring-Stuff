import re

# Strong Password Classification:
# At least 8 characters
# Contains lower and uppercase characters
# Contains at least 1 character

def detectStrongPW(password):
    strongPWStatus = True

    # if the length of the password is less than 8, no uppercase, lowercase or numeric characters are found, strongPWStatus
    # is set to false to indicate the password is not strong
    if len(password) < 8:
        strongPWStatus = False
    elif re.search('[a-z]+', password) == None:
        strongPWStatus = False
    elif re.search('[A-Z]+', password) == None:
        strongPWStatus = False
    elif re.search('[0-9]+', password) == None:
        strongPWStatus = False

    return strongPWStatus



userPW = input("Please enter your password:\n")

# if the password is considered strong, an message is printed indicating a strong password
if detectStrongPW(userPW) == True:
    print("Strong Password Detected.")
# else, a message is printed indicating a weak password
else:
    print("Strong Password Not Detected.")