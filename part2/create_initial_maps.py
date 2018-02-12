import random
from part2 import geneticAlgorithm


def map_size ():
    
    maprow = int(input("How many rows in the map? \n"))
    mapcol = int(input("How many cols in the map? \n"))
    
    return maprow, mapcol


def initial_map (maprow, mapcol):
    matrix = {}
    for i in range(maprow):
        for j in range(mapcol):
            k = random.randint(0,9)
            matrix[i,j] = k
    
    matrix[0,0] = "X"
    matrix[1,1] = "S"
    
    return matrix


mapsize = map_size()
maprow = mapsize[0]
mapcol = mapsize[1]

initial_map = initial_map(maprow, mapcol)

print(initial_map)


def map_status (maprow, mapcol, initial_map):
    
    i=0
    j=0
    m=0
    h=0
    k=0
    
    industrial_number = int(input("How many industrial tiles on the map? \n"))
    residential_number = int(input("How many residential tiles on the map? \n"))
    commercial_number = int(input("How many commercial tiles on the map? \n"))
    
    map_status = {}
    
    for i in range(maprow):
        for j in range(mapcol):
            map_status[i,j]=0
    

    
    while m < industrial_number:
        random_row = random.randint(0,maprow-1)
        random_col = random.randint(0,mapcol-1)
        if initial_map[random_row, random_col] == "X":
            continue
        map_status[random_row, random_col] = "I"
        m += 1

    
    while h < residential_number:
        random_row = random.randint(0,maprow-1)
        random_col = random.randint(0,mapcol-1)
        if map_status[random_row, random_col] != 0 or initial_map[random_row, random_col] == "X":
            continue
        map_status[random_row, random_col] = "R"
        h += 1
        
    while k < commercial_number:
        random_row = random.randint(0,maprow-1)
        random_col = random.randint(0,mapcol-1)
        if map_status[random_row, random_col] != 0 or initial_map[random_row, random_col] == "X":
            continue
        map_status[random_row, random_col] = "C"
        k += 1

    return map_status


initial_map = {(0, 0): 6, (0, 1): 9, (0, 2): 6, (0, 3): 5, (0, 4): 9, (0, 5): 8, (0, 6): 6, (1, 0): 6, (1, 1): 7, (1, 2): 5, (1, 3): 6, (1, 4): 5, (1, 5): 5, (1, 6): 6, (2, 0): 1, (2, 1): 4, (2, 2): 3, (2, 3): 5, (2, 4): 8, (2, 5): 'S', (2, 6): 8, (3, 0): 7, (3, 1): 6, (3, 2): 9, (3, 3): 4, (3, 4): 4, (3, 5): 4, (3, 6): 0, (4, 0): 0, (4, 1): 4, (4, 2): 7, (4, 3): 'X', (4, 4): 9, (4, 5): 9, (4, 6): 1, (5, 0): 1, (5, 1): 3, (5, 2): 5, (5, 3): 3, (5, 4): 9, (5, 5): 2, (5, 6): 6, (6, 0): 8, (6, 1): 2, (6, 2): 6, (6, 3): 5, (6, 4): 4, (6, 5): 2, (6, 6): 4}
# map_status = {(0, 0): 'I', (0, 1): 'R', (0, 2): 'C', (0, 3): 0, (0, 4): 0, (0, 5): 0, (0, 6): 0, (1, 0): 0, (1, 1): 'R', (1, 2): 0, (1, 3): 0, (1, 4): 'R', (1, 5): 0, (1, 6): 0, (2, 0): 'R', (2, 1): 0, (2, 2): 'C', (2, 3): 0, (2, 4): 0, (2, 5): 0, (2, 6): 0, (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 0, (3, 5): 0, (3, 6): 0, (4, 0): 'C', (4, 1): 0, (4, 2): 'R', (4, 3): 0, (4, 4): 0, (4, 5): 0, (4, 6): 'C', (5, 0): 0, (5, 1): 0, (5, 2): 0, (5, 3): 0, (5, 4): 'I', (5, 5): 0, (5, 6): 0, (6, 0): 0, (6, 1): 0, (6, 2): 'I', (6, 3): 0, (6, 4): 'I', (6, 5): 0, (6, 6): 'C'}
# new_map = map(maprow, mapcol, initial_map, map_status)
# ori_map = map(maprow, mapcol, initial_map, initial_map)
# print(ori_map)
# #print(new_map)
# test_map = map(maprow, mapcol, initial_map, new_map.create_map())
# new_map.fitness()
# #print(new_map.fitness())
# print(test_map)
#print(str(test_map.find_terrain_in_distance(new_map.create_map(),3,'C',2,2)))
geneticAlgorithm.geneticRun(initial_map, 7, 7, 3, 3, 3, 10)


