import pyinputplus as pyip



kBreadChoices = ["wheat", "white", "sourdough"]
kProteinChoices = ["chicken", "turkey", "ham", "tofu"]
kCheeseChoices = ["cheddar", "Swiss", "Mozzarella"]



def sandwichMaker():
    sandwichPrice = 0.0
    option = ""

    # prompt user for bread type in form of a numbered menu
    option = pyip.inputMenu(kBreadChoices, numbered=True)

    # if statements to determine what option the user picked, and will add the price of ingredient to the sandwich total
    if option == kBreadChoices[0]:
        sandwichPrice += 1
    elif option == kBreadChoices[1]:
        sandwichPrice += 1.3
    elif option == kBreadChoices[2]:
        sandwichPrice += 1.7

    # prompt user for protien options in form of a numbered menu
    option = pyip.inputMenu(kProteinChoices, numbered=True)

    # if statements to determine what option the user picked, and will add the price of ingredient to the sandwich total
    if option == kProteinChoices[0]:
        sandwichPrice += 1.5
    elif option == kProteinChoices[1]:
        sandwichPrice += 2
    elif option == kProteinChoices[2]:
        sandwichPrice += 1
    elif option == kProteinChoices[3]:
        sandwichPrice += 2.5

    # asks user if they want to add cheese, if the answer is yes, will then show a menu of cheese options
    if pyip.inputYesNo("Would you like to add cheese?\n") == 'yes':
        option = pyip.inputMenu(kCheeseChoices, numbered=True)

        # if statements to determine what option the user picked, and will add the price of ingredient to the sandwich total
        if option == kCheeseChoices[0]:
            sandwichPrice += 1
        elif option == kCheeseChoices[1]:
            sandwichPrice += 1.5
        elif option == kCheeseChoices[2]:
            sandwichPrice += 2

    # asks user if they want to add mayo, mustard, lettuce, or tomatoes, if the answer is yes, the sandwich total is increased
    if pyip.inputYesNo("Would you like to add mayo, mustard, lettuce, or tomatoes?\n") == 'yes':
        sandwichPrice += 2

    # prompts user for value on how many sandwiches they would like to order, will then multiply sandwich total with input
    option = pyip.inputInt("How many sandwiches would you like to order?\n", greaterThan=0)
    sandwichPrice = sandwichPrice * option

    # round and print the sandwich total price
    sandwichPrice = round(sandwichPrice, 2)
    print(f"Your total is: ${sandwichPrice}\n")



sandwichMaker()