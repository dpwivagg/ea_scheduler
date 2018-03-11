import random
from Assignment1.part2 import geneticAlgorithm
from Assignment1.part2.hill_climbing import urban_planning, print_board


def map_size ():
    
    maprow = int(input("How many rows in the map? \n"))
    mapcol = int(input("How many cols in the map? \n"))
    num_waste = int(input("How many waste sites in the map? \n"))
    num_view = int(input("How many view sites in the map? \n"))
    return maprow, mapcol,num_waste,num_view


def init_map (maprow, mapcol,num_waste,num_view):
    matrix = {}
    for i in range(maprow):
        for j in range(mapcol):
            k = random.randint(0,9)
            matrix[i,j] = k
    matrix = {}

    for i in range(maprow):
        for j in range(mapcol):
            k = random.randint(0, 9)
            matrix[i, j] = k

    for i in range(num_waste):
        random_row = random.randint(0, maprow - 1)
        random_col = random.randint(0, mapcol - 1)
        matrix[random_row, random_col] = "X"

    m = 0
    while m < num_view:
        random_row = random.randint(0, maprow - 1)
        random_col = random.randint(0, mapcol - 1)
        if matrix[random_row, random_col] == "X":
            continue
        matrix[random_row, random_col] = "S"
        m += 1
    return matrix


# print(initial_map)
def map_status (maprow, mapcol, initial_map):
    
    i=0
    j=0
    m=0
    h=0
    k=0
    
    industrial_number = int(input("How many industrial tiles on the map? \n"))
    residential_number = int(input("How many residential tiles on the map? \n"))
    commercial_number = int(input("How many commercial tiles on the map? \n"))
    last_time = float(input("How long do you want it to run ? \n"))
    algorithm = str(input('What algorithm do you want to use? a. Genetic b.Hill Climb\n'))
    while algorithm!='a' and  algorithm!='b':
        algorithm = input('Invalid input! What algorithm do you want to use? a. Genetic b.Hill Climb\n')
    if algorithm == 'a':
        print("Running Genetic Algorithm for "+ str(last_time)+ " second(s)!")
        geneticAlgorithm.geneticRun(initial_map, maprow, mapcol, industrial_number, residential_number, commercial_number, last_time)
    elif algorithm =='b':
        print("Running Hill Climb for "+ str(last_time)+ " second(s)!")
        map_status = {}
        for i in range(maprow):
            for j in range(mapcol):
                map_status[i, j] = 0
        while m < industrial_number:
            random_row = random.randint(0, maprow - 1)
            random_col = random.randint(0, mapcol - 1)
            if initial_map[random_row, random_col] == "X":
                continue
            map_status[random_row, random_col] = "I"
            m += 1

        while h < residential_number:
            random_row = random.randint(0, maprow - 1)
            random_col = random.randint(0, mapcol - 1)
            if map_status[random_row, random_col] != 0 or initial_map[random_row, random_col] == "X":
                continue
            map_status[random_row, random_col] = "R"
            h += 1

        while k < commercial_number:
            random_row = random.randint(0, maprow - 1)
            random_col = random.randint(0, mapcol - 1)
            if map_status[random_row, random_col] != 0 or initial_map[random_row, random_col] == "X":
                continue
            map_status[random_row, random_col] = "C"
            k += 1
        for i in range(maprow):
            for j in range(mapcol):
                map_status[i, j] = 0

        h = urban_planning(maprow, mapcol, map_status, initial_map,industrial_number,residential_number,commercial_number,last_time)
        for row in range(maprow):
            for col in range(mapcol):
                if h[1][0][(row, col)] == "I":
                    initial_map[(row, col)] = "I"

                if h[1][0][(row, col)] == "C":
                    initial_map[(row, col)] = "C"

                if h[1][0][(row, col)] == "R":
                    initial_map[(row, col)] = "R"
        print("\n")
        print("Final Urban Planning: ")
        format = print_board(initial_map, maprow, mapcol)
        print(format)
        print("Fitness:" + str(h[1][1]))
        print("Urban planning time: " + str(h[0]))
    pass

def take_input():
    maprow = 0
    mapcol = 0
    num_waste = 0
    num_view = 0
    while True:
        mapsize = map_size()
        maprow = mapsize[0]
        mapcol = mapsize[1]
        num_waste = mapsize[2]
        num_view = mapsize[3]
        initial_map = init_map(maprow, mapcol, num_waste, num_view)
        map_status(maprow, mapcol, initial_map)
        ans = str(input('Do you want to play again? Y/N\n'))
        while ans!='Y'and ans!='N':
            ans= str(input('Please type in the correct value. Do you want to play again? Y/N \n'))
        if ans == 'N':
            break
    pass

take_input()



