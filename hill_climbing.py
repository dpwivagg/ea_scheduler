from copy import deepcopy
import datetime

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
  
    answers = [] 
    attackedQueens = heuristic_function(status) 
  
    for key,value in successor.items():  
        if value < attackedQueens:  
            attackedQueens = value  
        
    for key,value in successor.items():  
        if value == attackedQueens:  
            answers.append(key)  
  
    if len(answers) > 0:  
        x = random.randint(0,len(answers)-1)  
        col = answers[x][0]  
        row = answers[x][1]
        cost = 10 + abs(status[col] - row)**2
        status[col] = row  
  
    return status, cost
  
    
def Queens(status):  
    status = board
    cost = 0
    expansion = 0
    starttime = datetime.datetime.now()
    print ("The start status:" + str(status))
   
    while heuristic_function(status) > 0: 
        one_move = hill_climbing(status)
        status = one_move[0]
        cost = cost + one_move[1]
        expansion += 1
        print (status) 
        print (heuristic_function(status))  
    
    endtime = datetime.datetime.now()
    print ("The final status is:" + str(status))  
    print ("The total cost is:" + str(cost))
    print ("The number of nodes expanded:" + str(expansion))
    print ("Cost time:" + str(endtime - starttime))

Queens(board)