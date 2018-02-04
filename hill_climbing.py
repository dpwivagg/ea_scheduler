from copy import deepcopy
import datetime

def heuristic_function (board):
    h = 10
    
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

heuristic_function(board)

def hill_climbing(status):  
    successor = {}    
    cost = 0
    
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
  
    if len(best_answers) > 0:  
        x = random.randint(0,len(best_answers)-1)  
        col = best_answers[x][0]  
        row = best_answers[x][1]
        cost = 10 + abs(status[col] - row)**2
        status[col] = row  
  
    return status, cost

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
    
def Queens(status):  
    status = board
    cost = 0
    expansion = 0
    path = 0
    starttime = datetime.datetime.now()
    print ("The start status:" + str(status))
   
    while heuristic_function(status) > 0: 
        one_move = hill_climbing(status)
        status = one_move[0]
        cost = cost + one_move[1]
        expansion += ((len(status))**2-len(status))
        path += 1
        print (status)
        print (__str__(status))
        print (heuristic_function(status))  
        
        # for restart: I m not sure about this part
        if expansion > 100:
            x = random.randint(0,len(status)-1)
            while status[x] - 1 >= 0:
                status[x] = status[x] - 1
    
    endtime = datetime.datetime.now()
    print ("The final status is:" + str(status))
    print(__str__(status))
    print ("The length of the solution path:" + str(path))
    print ("The total cost is:" + str(cost))
    print ("The number of nodes expanded:" + str(expansion))
    print ("Cost time:" + str(endtime - starttime))

Queens(board)
