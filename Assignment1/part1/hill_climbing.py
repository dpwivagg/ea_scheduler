from copy import deepcopy
import datetime
import random
# Create the heuristic function for hill climbing.
def heuristic_function (board):
    h = 10
    
    # Check the number of attacked queens.
    for i in range(len(board)):
        for j in range(i + 1,len(board)):
            if board[i] == board[j]:
                h += 1   
            check_diagonal = j - i
            if board[i] == board[j] - check_diagonal or board[i] == board[j] + check_diagonal:
                h += 1
    
    if h == 10:
        h = 0
    
    return h


# Restart to get a new status randomly.
def restart(status):
    status = get_board(len(status))  
    
    return status

# Compute the maximum heuristic based on the size of the board.
# This would be used in checking if the heuristic is large enough to restart or not. 
def max_heuristic(status):
    maxheuristic = (1 + len(status)) * len(status)/2
    
    return maxheuristic

# Hill climbing function
def hill_climbing(status):  
    successor = {}    
    cost = 0
    
    # Check all possibilities. 
    # Calculate the heuristic for each of them and store the positions and heuristics into a dict.
    for col in range(len(status)):     
        for row in range(len(status)):
            if status[col] == row:  
                continue  
            status_copy = deepcopy(status)
            status_copy[col] = row  
            successor[(col,row)] = heuristic_function(status_copy)  
  
    best_answers = [] 
    attackedQueens = heuristic_function(status) 
    
    for key,value in successor.items():  
        if value < attackedQueens:  
            attackedQueens = value  
        
    for key,value in successor.items():  
        if value == attackedQueens:  
            best_answers.append(key)  
    
    # Choose a status randomly from the answer list with smallest heuristic.
    if len(best_answers) > 0:  
        x = random.randint(0,len(best_answers)-1)  
        col = best_answers[x][0]  
        row = best_answers[x][1]
        cost = 10 + abs(status[col] - row)**2
        status[col] = row  
    
    # Check if a new status with a lower heuristic exists or not.
    # If the heuristic is increasing, restart to get a new board status.
    if len(best_answers) == 0:
        restart(status)
        print("Restart because heuristic is increasing!")
    
    # If the heuristic is more than 80% of the maximum heuristic, restart.
    if heuristic_function(status) > (max_heuristic(status)*0.8):
        restart(status)
        print("Restart because heuristic is too high!")
  
    return status, cost

# Print what the board looks like.
def __str__(status):
    string = ""
    for row in range(0, len(status)):
        string = string + "\n|"
        for col in range(0, len(status)):
            if row == status[col]:
                string = string + "Q|"
            else:
                string = string + " |"
    return string

# Run with hill climbing
def Queens(board):
    status = board
    cost = 0
    expansion = 0
    path = 0
    sideways_count = 0
    starttime = datetime.datetime.now()
    print ("The start status:" + str(status))
   
    while heuristic_function(status) > 0: 
        heuristic_now = heuristic_function(status)
        one_move = hill_climbing(status)
        status = one_move[0]
        cost = cost + one_move[1]
        expansion += ((len(status))**2-len(status))
        path += 1
        
        # If stucks in sideways, need to restart to help it out.
        if heuristic_now == heuristic_function(status):
            sideways_count += 1
            if sideways_count > len(status):
                restart(status)
                sideways_count = 0
                print("Sideways!Restart board: " + str(status))
                
        print (status)
        print (__str__(status))
        print (heuristic_function(status))  
    
    endtime = datetime.datetime.now()
    print ("The final status is: " + str(status))
    print(__str__(status))
    print ("The length of the solution path: " + str(path))
    print ("The total cost is: " + str(cost))
    print ("The number of nodes expanded: " + str(expansion))
    print ("The branching factor: " + str(expansion/path))
    print ("Cost time: " + str(endtime - starttime))

def get_board(size):
    board = []
    for i in range(size):
        k = random.sample(range(0,size-1),1)
        board = board + k
        i += 1
    print(board)
    return board


