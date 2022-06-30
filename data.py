import json
file = open("boards.json", "r")
#outFile = open("cleanedData", "w")

def cleanData(file):
    #outFile = open("cleanedData", "w")
    boards = []
    choices = []
    count = 1
    for line in file:
        if count%2 == 1:
            b = json.loads(line.split(":")[0])
            c = json.loads(line.split(":")[-1])
            if c != " ":
                choices.append(c)
            for row in range(len(b)):
                for col in range(len(b[row])):
                    if b[row][col] == -9999:
                        b[row][col] = -1
                    elif b[row][col] == 9999:
                        b[row][col] = -2
            boards.append(b)
        count += 1
        print("cleaning line: ", count, "\n")
    #outFile.write(json.dumps(boards))
    return boards, choices

def findFlags(boards, choices):
    outputs = []
    noflagBoard = []
    for c in range(len(choices) - 1):
        coords = choices[c]
        if boards[c+1][coords[0]][coords[1]] == -2:
            #print("on board ", c, " we flagged spot ", coords, " which is equal to spot: ", 400 + 20*coords[0] + coords[1], "\n")
            #outputs.append(400 + 20*coords[0] + coords[1])
            boards[c+1][coords[0]][coords[1]] = -1
        #elif boards[c+1][coords[0]][coords[1]] == -1 and boards[c][coords[0]][coords[1]] == -2:
            #print("on board ", c, " we unflagged spot ", coords, " which is equal to spot: ", 800 + 20*coords[0] + coords[1], "\n")
            #outputs.append(800 + 20*coords[0] + coords[1])
            #continue
        else:
            #print("on board ", c, " we clicked spot ", coords, " which is equal to spot: ", 20*coords[0] + coords[1], "\n" "\n")
            outputs.append(20*coords[0] + coords[1])
            noflagBoard.append(boards[c])

    print(len(noflagBoard), len(outputs))
    return(outputs, noflagBoard)

def setOutputs(boards, choices):
    outputs = []
    for out in choices:
        outputs.append(20*out[0] + out[1])
    #print(outputs)
    return outputs

#boa is a list of boards where each board is a 2D matrix row*col
#cho is a list of the choices made
#outputs is the spot that was chosen
#boa, cho = cleanData(file)
#outputs = findFlags(boa, cho)

#print(len(boa[:-1]), len(outputs))
