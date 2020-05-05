# Functions:   tablePrinter()
# Description: takes in a list of string lists and prints each column to the screen formatted so 
#              that the end of each word in the column aligns
# Parameters:  table: a list containing lists of strings to be printed
# Return:      N/A
def tablePrinter(table):
    # initializes list to keep track of longest length of word in each column
    colWidths = [0] * len(table)

    # loop that goes through each word in each column and gathers the length of the longest word in each column
    for i in range(len(table)):
        for j in range(len(table[i])):
            # if the length of the current word in the table is longer than the recorded length in that column,
            # the length of the current word overwrites the value currently recorded
            if len(table[i][j]) > colWidths[i]:
                colWidths[i] = len(table[i][j])

    # assumes that each list is the same length, this loop will iterate through each word in the list to
    # and print each string
    for x in range(len(table[0])):
        # prints each word in the row while padding it with the longest length word in the column
	    for y in range(len(table)):
		    print(table[y][x].rjust(colWidths[y]), end = ' ')
	    print('')



tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

tablePrinter(tableData)