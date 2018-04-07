from Assignment4.gameBoard import boardObject

board_rows = 6
board_column = 7
optimistic_value = 20
goal_value = 5
pit_value = -1
empty_value = 0

def actualMove():
    return


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

for i in range(board_rows+1):
    game_board[i,7] = boardObject("b", optimistic_value, None)

for i in range(board_column+1):
    game_board[6,i] = boardObject("b", optimistic_value, None)
