import random
from Assignment4.gameBoard import boardObject

def decideMove(y_move, x_move, left):
    actualX = 0
    actualY = 0
    if left:
        if y_move > 0:
            actualX = +1
            actualY = 0
        elif y_move < 0:
            actualX = -1
            actualY = 0
        elif x_move < 0:
            actualX = 0
            actualY = +1
        elif x_move > 0:
            actualX = 0
            actualY = -1
    else:
        if y_move > 0:
            actualX = -1
            actualY = 0
        elif y_move < 0:
            actualX = +1
            actualY = 0
        elif x_move < 0:
            actualX = 0
            actualY = -1
        elif x_move > 0:
            actualX = 0
            actualY = +1
    return actualY, actualX


def actualMove(action):
    x_move = action[1]
    y_move = action[0]
    x_current = current_state[1]
    y_current = current_state[0]
    move = None
    randomNum = random.randint(1, 100)
    print(randomNum)
    if randomNum in range(1, 70):
        # Move as expected
        move = action
    elif randomNum in range(71, 80):
        # Moves 90 degrees to the right
        y_move, x_move = decideMove(y_move,x_move, False)
        a = game_board.get((y_current + y_move, x_current + x_move), None)
        if a is None:
            move = action
        else:
            move = (y_move, x_move)
    elif randomNum in range(81, 90):
        # Moves 90 degrees to the left
        y_move, x_move = decideMove(y_move, x_move, True)
        a = game_board.get((y_current + y_move, x_current + x_move), None)
        if a is None:
            move = action
        else:
            move = (y_move, x_move)
    elif randomNum in range(91, 100):
        # Moves forward 2 squares
        a = game_board.get((y_current+ y_move, x_current + x_move), None)
        if a.getType() == "g" or a.getType() == "p":
            move = action
        else:
            a = game_board.get((y_current + 2*y_move, x_current + 2*x_move), None)
            if a is None:
                move = action
            else:
                move = (y_move*2, x_move*2)
    return current_state[0] + move[0], current_state[1] + move[1]


board_rows = 6
board_column = 7
optimistic_value = 20
goal_value = 5
pit_value = -1
empty_value = 0
current_state = None
game_board = {}

# This is for setting up the table.

for i in range(board_column):
    for j in range( board_rows):
        game_board[j, i] = boardObject("n", optimistic_value, empty_value)

game_board[2,2] = boardObject("p", optimistic_value, pit_value)
game_board[2,3] = boardObject("p", optimistic_value, pit_value)
game_board[3,1] = boardObject("p", optimistic_value, pit_value)
game_board[3,5] = boardObject("p", optimistic_value, pit_value)
game_board[4,2] = boardObject("p", optimistic_value, pit_value)
game_board[4,3] = boardObject("p", optimistic_value, pit_value)
game_board[4,4] = boardObject("p", optimistic_value, pit_value)
game_board[3,2] = boardObject("g", optimistic_value, goal_value)







