import json
file = open("boards.json", "r")

def cleanData(file):
    boards = []
    choices = []
    count = 1
    for line in file:
        if count%2 == 1:
            b = json.loads(line.split(":")[0])
            c = json.loads(line.split(":")[-1])
            if c != " ":
                choices.append(c)
            boards.append(b)
        count += 1
    return boards, choices

def findFlags(boards, choices):
    outputs = []
    for c in range(len(choices) - 1):
        coords = choices[c]
        if boards[c+1][coords[0]][coords[1]] == 9999:
            #print("on board ", c, " we flagged spot ", coords, " which is equal to spot: ", 400 + 20*coords[0] + coords[1], "\n")
            outputs.append(400 + 20*coords[0] + coords[1])
        elif boards[c+1][coords[0]][coords[1]] == -9999 and boards[c][coords[0]][coords[1]] == 9999:
            #print("on board ", c, " we unflagged spot ", coords, " which is equal to spot: ", 800 + 20*coords[0] + coords[1], "\n")
            outputs.append(800 + 20*coords[0] + coords[1])
        else:
            #print("on board ", c, " we clicked spot ", coords, " which is equal to spot: ", 20*coords[0] + coords[1], "\n" "\n")
            outputs.append(20*coords[0] + coords[1])

    return(outputs)

#boa is a list of boards where each board is a 2D matrix row*col
#cho is a list of the choices made
#outputs is the spot that was chosen
#boa, cho = cleanData(file)
#outputs = findFlags(boa, cho)

#print(len(boa[:-1]), len(outputs))