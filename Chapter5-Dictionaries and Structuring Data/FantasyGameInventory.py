# Function:    displayInventory()
# Description: takes in an inventory and displays the contents to the screen
# Parameters:  inventoryToDisplay: the inventory(dictionary) that will be displayed to the screen 
# Returns:     N/A
def displayInventory(inventoryToDisplay):
    numOfItems = 0

    print('Inventory:')

    # for loop that displays each inventory item, and keeps track of the total items
    for items, num in inventoryToDisplay.items():
        print(str(num) + ' ' + items)
        numOfItems += num
    
    print('Total Items: ' + str(numOfItems))



# Function:    addToInventory()
# Description: takes in an inventory and list of loot items to add to the inventory
# Parameters:  inventoryToAddTo: the inventory(dictionary) that will have items added to it
#              itemsToAdd: a list of items to be added into the player inventory
# Returns:     N/A
def addToInventory(inventoryToAddTo, itemsToAdd):
    
    # foreach loop that adds loot items into the player inventory
    for item in itemsToAdd:
        # if the current item to be added already exists in the inventory, the value is incremented
        if item in inventoryToAddTo:
            inventoryToAddTo[item] += 1
        # else, the item is added to the inventory with a value of 1
        else:
            inventoryToAddTo[item] = 1



inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inventory, dragonLoot)
displayInventory(inventory)
