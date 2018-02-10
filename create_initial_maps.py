import random

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


map_status = map_status(maprow, mapcol, initial_map)
print(map_status)