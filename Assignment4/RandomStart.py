import random
def RandomStart():
    game_board={}

    for i in range (0,6):
        for j in range (0,7):
            game_board[i,j]= 0.0

    game_board[2, 2] = "p"
    game_board[2, 3] = "p"
    game_board[3, 1] = "p"
    game_board[3, 5] = "p"
    game_board[4, 2] = "p"
    game_board[4, 3] = "p"
    game_board[4, 4] = "p"
    game_board[3, 2] = "p"

    row = random.randint(1, 5)
    column = random.randint(1,6)

    while game_board[row,column] == "p":
        row =random.randint(1,5)
        column = random.randint(1, 6)

    return row, column




