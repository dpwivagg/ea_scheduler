import random
from Assignment4.gameBoard import boardObject
from Assignment4.input import input_line
import numpy as np


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
        if a is None:
            move = action
        else:
            if a.getType() == "g" or a.getType() == "p":
                move = action
            else:
                a = game_board.get((y_current + 2*y_move, x_current + 2*x_move), None)
                if a is None:
                    move = action
                else:
                    move = (y_move*2, x_move*2)
    return current_state[0] + move[0], current_state[1] + move[1]


def updateQ(state1, action1, reward, state2, action2):
    q_current = q_values.get((state1, action1),0)
    q_next = q_values.get((state2, action2),0)
    q_values[(state1, action1)] = q_current + 0.5*(reward + 0.7*q_next - q_current)


def choose_action(state, epsilon):
    (i, j) = state
    actions = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    if random.random() < epsilon:
        action = random.choice(actions)
    else:
        moves = [game_board.get(a, None) for a in actions]
        q = [q_values.get((state,x),0) for x in moves if x is not None]
        maxQ = max(q)
        count = q.count(maxQ)
        # if count > 1:
        #     best = [i for i in range(len(actions)) if q[i] == maxQ]
        #     i = random.choice(best)
        # else:
        #     i = q.index(maxQ)
        i = q.index(maxQ)
        action = actions[i]

    return action


def randomStart():
    current_state = None
    while current_state is None:
        current_state = random.choice(list(game_board.keys()))
        if game_board[current_state].getType() != "n":
            current_state = None
    return current_state
    # row = random.randint(0, board_rows-1)
    # column = random.randint(0,board_column-1)
    # while game_board[row,column].getType() == "p" or game_board[row,column].getType() == "g":
    #     row = random.randint(0, board_rows - 1)
    #     column = random.randint(0, board_column - 1)
    #
    # return (row, column)


(goal_value, pit_value, eachmove, giveup, numiteration, epsilon) = input_line()

board_rows = 6
board_column = 7
optimistic_value = 20
# goal_value = 5
# pit_value = -1
empty_value = 0
current_state = None
last_action = None
game_board = {}

q_values = {}

# This is for setting up the table.

for i in range(board_column):
    for j in range( board_rows):
        game_board[j, i] = boardObject("n", empty_value - eachmove)

game_board[2,2] = boardObject("p", pit_value - eachmove)
game_board[2,3] = boardObject("p", pit_value - eachmove)
game_board[3,1] = boardObject("p", pit_value - eachmove)
game_board[3,5] = boardObject("p", pit_value - eachmove)
game_board[4,2] = boardObject("p", pit_value - eachmove)
game_board[4,3] = boardObject("p", pit_value - eachmove)
game_board[4,4] = boardObject("p", pit_value - eachmove)
game_board[3,2] = boardObject("g", goal_value - eachmove)






for i in range(0, numiteration):
    current_state = randomStart()
    while game_board[current_state].getType() != "g":
        desired_action = choose_action(current_state, epsilon)
        print(tuple(np.subtract(current_state,desired_action)))
        new_state = actualMove(tuple(np.subtract(current_state, desired_action)))
        if last_action is not None:
            updateQ(last_state, last_action, game_board[last_state].getReward(), current_state, desired_action)
        last_state = current_state
        current_state = new_state
        print(current_state)
        last_action = desired_action

        # TODO: add break for falling into pit and giving up

