
# coding: utf-8

# In[39]:

import random
from copy import deepcopy
from datetime import datetime


#randomly generate an urban map including "X" and "S"
# randomly set the location of industrial, residential and commercial tiles as initial status
def get_map_status(maprow, mapcol, initial_map, i_number, r_number, c_number):
    m = 0
    h = 0
    k = 0

    # industrial_number = int(input("How many industrial tiles on the map? \n"))
    # residential_number = int(input("How many residential tiles on the map? \n"))
    # commercial_number = int(input("How many commercial tiles on the map? \n"))

    map_status = {}

    for i in range(maprow):
        for j in range(mapcol):
            map_status[i, j] = 0

    while m < i_number:
        random_row = random.randint(0, maprow - 1)
        random_col = random.randint(0, mapcol - 1)
        if initial_map[random_row, random_col] == "X":
            continue
        map_status[random_row, random_col] = "I"
        m += 1

    while h < r_number:
        random_row = random.randint(0, maprow - 1)
        random_col = random.randint(0, mapcol - 1)
        if map_status[random_row, random_col] != 0 or initial_map[random_row, random_col] == "X":
            continue
        map_status[random_row, random_col] = "R"
        h += 1

    while k < c_number:
        random_row = random.randint(0, maprow - 1)
        random_col = random.randint(0, mapcol - 1)
        if map_status[random_row, random_col] != 0 or initial_map[random_row, random_col] == "X":
            continue
        map_status[random_row, random_col] = "C"
        k += 1

    return map_status


def initial_map (maprow, mapcol,num_waste,num_view):
    matrix = {}
    
    for i in range(maprow):
        for j in range(mapcol):
            k = random.randint(0,9)
            matrix[i,j] = k   

    for i in range(num_waste):
        random_row = random.randint(0,maprow-1)
        random_col = random.randint(0,mapcol-1)
        matrix[random_row, random_col] = "X"
 
    m=0
    while m < num_view:
        random_row = random.randint(0,maprow-1)
        random_col = random.randint(0,mapcol-1)
        if matrix[random_row, random_col] == "X":
            continue
        matrix[random_row, random_col] = "S"
        m += 1
    
    return matrix

# mapsize = map_size()
# maprow = mapsize[0]
# mapcol = mapsize[1]
# waste = mapsize[2]
# view = mapsize[3]
# initial_map = initial_map(maprow, mapcol)

#print map in a matrix format
def print_board(map, maprow, mapcol):
        string = ""
        for row in range(0, maprow):
            string = string + "\n|"
            for column in range(0, mapcol):
                if map[row, column] == 0:
                    string = string + "0|"
                else:
                    string = string + str(map[row, column]) + "|"

        return string

#get the number of industrial tiles, residential tiles and commercial tiles

#define the heuristic function
#Fitness= -build difficulty + bonus - penalty
def heuristic_function(maprow, mapcol, map_status, initial_map):
    
    heuristic = 0
    copymap = deepcopy(initial_map)
    
    # Compute the building cost of the initial status
    for row in range(maprow):      
        for col in range(mapcol):     
            if map_status[row, col] == "I":
                if type(initial_map[row, col])==int:
                    heuristic -= initial_map[row, col]
            elif map_status[row, col] == "C":
                if type(initial_map[row, col])==int:
                    heuristic -= initial_map[row, col]
            elif map_status[row, col] == "R":
                if type(initial_map[row, col])==int:
                    heuristic -= initial_map[row, col]
              
    # combining two maps
    for row in range(maprow):
        for col in range(mapcol): 
            if map_status[(row, col)] == "I":
                copymap[(row, col)] = "I"
            if map_status[(row, col)] == "C":
                copymap[(row, col)] = "C"
            if map_status[(row, col)] == "R":
                copymap[(row, col)] = "R"
    
    # Computing the fitness (penalty and bonus)
    for row in range(maprow): 
        for col in range(mapcol):
            
            if copymap[row,col]=="R":
                X_row = row
                X_col = col
                
                for i in range(maprow): 
                    for j in range(mapcol):
                        if copymap[i,j] == "C": 
                            I_row = i
                            I_col = j
                            difference = abs(I_row - X_row) + abs(I_col - X_col)
                            if difference < 4:
                                heuristic +=5       
                        if copymap[i,j] == "I":
                            I_row = i
                            I_col = j
                            difference = abs(I_row - X_row) + abs(I_col - X_col)
                            if difference < 4:
                                heuristic -=5
                        if copymap[i,j] == "X":
                            I_row = i
                            I_col = j
                            difference = abs(I_row - X_row) + abs(I_col - X_col)
                            if difference < 3:
                                heuristic -=20
                        if copymap[i,j] == "S":
                            I_row = i
                            I_col = j
                            difference = abs(I_row - X_row) + abs(I_col - X_col)
                            if difference < 3:
                                heuristic +=10
        
            elif copymap[row,col]=="C":
                X_row = row
                X_col = col
                
                for i in range(maprow): 
                    for j in range(mapcol):
                        if copymap[i,j] == "X":
                            I_row = i
                            I_col = j
                            difference = abs(I_row - X_row) + abs(I_col - X_col)
                            if difference < 3:
                                heuristic -=20
                        elif copymap[i,j] == "R":
                            I_row = i
                            I_col = j
                            difference = abs(I_row - X_row) + abs(I_col - X_col)
                            if difference < 4:
                                heuristic +=5
                        elif copymap[i,j] == "C": 
                            I_row = i
                            I_col = j
                            difference = abs(I_row - X_row) + abs(I_col - X_col)
                            if difference < 3 and difference !=0:
                                heuristic -= 5

            elif copymap[row,col]=="I":
                X_row = row
                X_col = col
                
                for i in range(maprow): 
                    for j in range(mapcol):
                        
                        if copymap[i,j] == "X":
                            I_row = i
                            I_col = j
                            difference = abs(I_row - X_row) + abs(I_col - X_col)
                            if difference < 3:
                                heuristic -=10
                        elif copymap[i,j] == "I":
                            I_row = i
                            I_col = j
                            difference = abs(I_row - X_row) + abs(I_col - X_col)
                            if difference < 3 and difference != 0:
                                 heuristic +=3
                                     
    return heuristic 

#define the function of doing hill climbing
def hill_climbing (maprow, mapcol, map_status, initial_map):
    move = {}
    candidate_move=[]
    occupy = []
    next_move =[]
   
    for key, value in map_status.items():
        if value == "I":
            occupy.append(key)
        elif value == "R":
            occupy.append(key)
        elif value == "C":
            occupy.append(key)
            
    for items in range(len(occupy)):    
        for row in range(maprow):
            for col in range(mapcol):
                if map_status[(row, col)] == 0 and initial_map[row,col]!="X":
                    copy_status = deepcopy(map_status)
                    copy_status[row,col]= map_status[occupy[items]]
                    copy_status[occupy[items]]=0
                    move[(row,col)]= heuristic_function(maprow, mapcol, copy_status, initial_map)
        get_max_i = max(move.items(), key=lambda x: x[1])
        get_max_i = get_max_i + (map_status[occupy[items]], occupy[items])
        candidate_move.append(get_max_i)

    fitness = heuristic_function(maprow, mapcol, map_status, initial_map)
    
    for items in range(len(candidate_move)):
        if candidate_move[items][1] > fitness:  
            fitness = candidate_move[items][1]  
        
    for items in range(len(candidate_move)):  
        if candidate_move[items][1] == fitness: 
            next_move.append(candidate_move[items])  
    
    if len(next_move) > 0:  
        x = random.randint(0,len(next_move)-1)  
        map_status[next_move[x][0]] =  map_status[next_move[x][3]]
        map_status[next_move[x][3]] = 0
       
    return map_status, fitness

#test module
def urban_planning(maprow, mapcol, map_status, initial_map,i_number,r_number,c_number,time):

    initial_copy = deepcopy(initial_map)
    initial_status = deepcopy(map_status)
    fitness = heuristic_function(maprow, mapcol, map_status, initial_map)
    time_cost = 0
    best_status = {}
    local_best=[]

    for row in range(maprow):
        for col in range(mapcol):
            if map_status[(row, col)] == "I":
                initial_copy[(row, col)] = "I"

            if map_status[(row, col)] == "C":
                initial_copy[(row, col)] = "C"

            if map_status[(row, col)] == "R":
                initial_copy[(row, col)] = "R"

    # print("The start status:")
    # format=print_board(initial_copy, maprow, mapcol)
    # print(format)
    # print("Fitness: "+str(fitness))

    start_time = datetime.now()
    
    one_move = hill_climbing(maprow, mapcol, map_status, initial_map)
    # print("one move:")
    # format=print_board(one_move[0], maprow, mapcol)
    # print(format)
    # print("Fitness: "+ str(one_move[1]) )


    while time_cost < time:
        
        while one_move[1] > fitness:
            map_status = one_move[0]
            fitness = one_move[1]
            one_move = hill_climbing(maprow, mapcol, map_status, initial_map)
            # print("one move:")
            format=print_board(one_move[0], maprow, mapcol)
            # print(format)
            # print("Fitness: " + str(one_move[1]) )
            time_now = datetime.now()
            time_cost=(time_now - start_time).total_seconds()

            if time_cost >= time:
                #print ("Time cost:" + str(time_cost))
                break

#   stuck on local optima, store the local optima status in local_best, then restart hill climbing
        local_best.append([map_status, fitness])
        if time_cost >= 10:
            break
        fitness = heuristic_function(maprow, mapcol, initial_status, initial_map)
        map_status = get_map_status(maprow, mapcol, initial_map, i_number, r_number, c_number)
        one_move = hill_climbing(maprow, mapcol, map_status, initial_map)
        
        # print("Restart to try again, new status is: ")
        # format=print_board(map_status, maprow, mapcol)
        # print(format)
        # print("Fitness: "+str(one_move[1]))
       
        end_time = datetime.now()
        time_cost = (end_time - start_time).total_seconds()

#   sort the status in local_cost through fitness value
    for i in range(len(local_best)):
        for j in range(i+1,len(local_best)):
            first = int(local_best[i][1])
            first_m = deepcopy(local_best[i][0])
            second = int(local_best[j][1])
            if first < second:
                local_best[i][1] = local_best[j][1]
                local_best[i][0] = local_best[j][0]
                local_best[j][1] = first
                local_best[j][0] = first_m

    return  time_cost, local_best[0]








