import random
from Assignment4.gameBoard import boardObject
from Assignment4.input import input_line


def actualMove(action):
    move = int
    randomNum = random.randint(1, 100)
    print(randomNum)
    if randomNum in range(1, 70):
        # Move as expected
        move = action
    elif randomNum in range(71, 80):
        # Moves 90 degrees to the right
        a = game_board.get((action[0], action[1]), None)
        if a is None:
            move = action
        else:
            move = a
    elif randomNum in range(81, 90):
        # Moves 90 degrees to the left
        move = 3
    elif randomNum in range(91, 100):
        # Moves forward 2 squares
        move = 4
    return move


def updateQ(state1, action1, reward, state2, action2):
    q_current = game_board.get((state1, action1))
    q_next = game_board.get((state2, action2))
    game_board[(state1, action1)] = q_current + 0.5*(reward + 0.7*q_next - q_current)


def choose_action(state, epsilon):
    (i, j) = state
    actions = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    if random.random() < epsilon:
        action = random.choice(actions)
    else:
        # TODO: Add try/catch to the line below
        q = [game_board.get(actions, None).getCurrentUtility for a in actions]
        maxQ = max(q)
        count = q.count(maxQ)
        if count > 1:
            best = [i for i in range(len(actions)) if q[i] == maxQ]
            i = random.choice(best)
        else:
            i = q.index(maxQ)

        action = actions[i]

    return action

def attempt_move():
    # TODO: Fill this in
    pass

(goal_value, pit_value, eachmove, giveup, numiteration, epsilon) = input_line()

board_rows = 6
board_column = 7
optimistic_value = 20
# goal_value = 5
# pit_value = -1
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



while current_state is None:
    current_state = random.choice(game_board.keys())
    if game_board[current_state].getType() != "n":
        current_state = None


for i in range(0, numiteration):
    while game_board[current_state].getType() != "g":
        desired_action = choose_action(current_state, epsilon)
        new_state = attempt_move(current_state, desired_action)
        if last_action is not None:
            updateQ(last_state, last_action, game_board[last_state].getReward(), current_state, desired_action)
        last_state = current_state
        current_state = new_state
        last_action = desired_action

        # TODO: add break for falling into pit and giving up

