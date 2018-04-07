# input format: sarsa 5 -2 -0.1 -3 10000 0.1

def input_line():
    line = input()
    line_split = line.split(" ")


    for i in range(len(line_split)):
        if i == 1:
            goal = float(line_split[1])
        if i == 2:
            pit = float(line_split[2])
        if i == 3:
            eachmove = float(line_split[3])
        if i == 4:
            giveup = float(line_split[4])
        if i == 5:
            numiteration = int(line_split[5])
        if i == 6:
            epsilon = float(line_split[6])


    return goal, pit, eachmove, giveup, numiteration, epsilon

