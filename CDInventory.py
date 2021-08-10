#--------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
#   DBiesinger, 2030-Jan-01, Created File
#   Garrett, 2021-Aug-8, Edited header
#   Garrett, 2021-Aug-8, Edited code
#--------------------------------------#

# -- DATA -- #
# Declare variables
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {'ID': '', 'Title': '', 'Artist': ''}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# -- PRESENTATION -- #
# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

# -- PROCESSING -- #
    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    #Load data to list
    if strChoice == 'l':
        objFile = open(strFileName, 'r')
        for line in objFile:
            value = []
            value.append(line.strip().split())
            for item in value:
                counter = 0 # Searches the other file and adds the text into the 2d list
                for element in item:
                    element = element[:-1]
                    counter += 1
                    if counter == 1:
                        dicRow['ID'] = element
                    elif counter == 2:
                        dicRow['Title'] = element
                    elif counter == 3:
                        dicRow['Artist'] = element
                        lstTbl.append(dicRow)
        objFile.close()
# -- PRESENTATION -- #
    #Add data to list
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ') 
        strArtist = input('Enter the Artist\'s Name: ')

# -- PROCESSING -- #
        dicRow = {'ID': strID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow) # Adds user input to the 2d list
    
    #Display list
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl: # Displays the CD library
            print(*row.values(), sep = ', ')
      
    #Delete data from list
    elif strChoice == 'd':
        userInput = int(input('Which entry number would you like to delete? (choose 1-' + str(len(lstTbl)) + ') '))
        userInput -= 1 # Deletes the user's chosen entry from the 2d list
        lstTbl.pop(userInput)
    #Save data to file    
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = '' # Writes data from the 2d list into the other file
            values = row.values()
            valuesList = list(values)
            for value in valuesList:
                strRow += str(value) + ', '
            strRow = strRow[:-2] + '\n'
            objFile.write(strRow)
        objFile.close()
    #Other
    else:
        print('Please choose either l, a, i, d, s or x!')
