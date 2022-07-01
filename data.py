#=======================================================
# Ryan Erickson, Manas Panachavati, Mitchell Aschmeyer
# data.py
# June 2022
# This project handles the data cleaup and prep for model.py
#======================================================

import json
import numpy as np

def cleanData(file):
    '''
    This function cleans the raw data from the provided json file and normalizes the data
    '''
    boards = []
    choices = []
    count = 1
    for line in file:
        if count%2 == 1:
            b = json.loads(line.split(":")[0])  #read in json array string
            c = json.loads(line.split(":")[-1])
            if c != " ":
                choices.append(c)
            for row in range(len(b)):
                for col in range(len(b[row])):      #fix data that is improperly scored
                    if b[row][col] == -9999:
                        b[row][col] = -1
                    elif b[row][col] == 9999:
                        b[row][col] = -2
            boards.append(b)
        count += 1
    return boards, choices

def findFlags(boards, choices):
    '''
    This function prepares the outputs for a clean data set that does
    include flag and unflag moves
    '''
    outputs = []
    noflagBoard = []
    for c in range(len(choices) - 1):
        coords = choices[c]
        if boards[c+1][coords[0]][coords[1]] == -2:     #check to see if this move was a flag or click
            boards[c+1][coords[0]][coords[1]] = -1      #fix data if it was a flag
        else:
            outputs.append(20*coords[0] + coords[1])    #store new value and the current board if it was not a flag
            noflagBoard.append(boards[c])

    print(len(noflagBoard), len(outputs))
    return(outputs, noflagBoard)

def setOutputs(boards, choices):
    '''
    This function prepares the outputs for a clean data set that does not
    include flag moves
    '''
    outputs = []
    for out in choices:
        outputs.append(20*out[0] + out[1])
    #print(outputs)
    return outputs

def prepData(file1, file2="NONE"):
    '''
    This function prepares data to be used in the neural network.
    file2 is used if there is extra data that needs to be cleaned more
    '''
    #use both board files and clean the data from them
    boards, choices = cleanData(file1)
    y = setOutputs(boards, choices)

    #perform extra steps if file2 is included for extra cleaning
    if file2 != "NONE":
        boards2, choices2 = cleanData(file2)
        y2, boards2 = findFlags(boards2, choices2)
        boards = boards + boards2
        y = y + y2

    x = []
    count = 0
    for board in boards:
        rows = []
        for row in board:
            rows = rows + row   #combine all rows for 1 board into a single (1, 400) array
        x.append(rows)
    x = np.array(x) #update to numpy array for keras
    y = np.array(y)

    return x, y
