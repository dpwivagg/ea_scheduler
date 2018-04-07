import random

def actualMove():
    move = int
    randomNum = random.randint(1, 100)
    print(randomNum)
    if randomNum in range(1, 70):
        # Move as expected
        move = 1
    elif randomNum in range(71, 80):
        # Moves 90 degrees to the right
        move = 2
    elif randomNum in range(81, 90):
        # Moves 90 degrees to the left
        move = 3
    elif randomNum in range(91, 100):
        # Moves forward 2 squares
        move = 4

    return move