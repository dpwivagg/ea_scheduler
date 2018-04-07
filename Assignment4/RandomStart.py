import random
def RandomStart():

    board={}

    for i in range (0,6):
        for j in range (0,7):
            board[i,j]= 0.0

    board[2, 2] = "p"
    board[2, 3] = "p"
    board[3, 1] = "p"
    board[3, 5] = "p"
    board[4, 2] = "p"
    board[4, 3] = "p"
    board[4, 4] = "p"
    board[3, 2] = "p"

    row = random.randint(0, 5)
    column = random.randint(0,6)

    while board[row,column] == "p":
        row =random.randint(0,5)
        column = random.randint(0, 6)

    return row, column




