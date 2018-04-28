# TODO: implement hill climbing algorithm
import random
from FinalProject.person import Person
from FinalProject.schedule import Schedule
from FinalProject.data_parser import read_data

def hill_climbing():
    candidate_move=[]
    fitness=0
    next_move=[]
    best_move=[]
    #choose the next step
    for items in range(len(candidate_move)):
        if candidate_move[items][1] > fitness:
            fitness = candidate_move[items][1]

    for items in range(len(candidate_move)):
        if candidate_move[items][1] == fitness:
            next_move.append(candidate_move[items])

    if len(next_move) > 0:
        x = random.randint(0, len(next_move) - 1)
        best_move = next_move[x]
    return best_move, fitness

role_list=["PRESENTER","INTRO","LEAD","DEBRIEF"]

def start():
    allpeople = read_data()
    sch= Schedule([],{},[])
    for person in allpeople:
        avaeventlist = []
        for i in range(0,21):
            if person.availabilities[i][0] != 0:
                avaeventlist.append(i+1)
        # print(avaeventlist)
        x = random.randint(1,len(avaeventlist))
        person.eventIDs = random.sample(avaeventlist, x)
        person.eventIDs.sort()

        for j in range(len(person.eventIDs)):
            x = random.randint(0,3)
            person.roles.append(role_list[x])

    # for person in allpeople:
    #     print(person.eventIDs)

    for i in range(1,22):
        for j in range(1,7):
            sch.events_avaibilities[i,j]=[]


    for person in allpeople:
        for i in range(len(person.eventIDs)):
            event = person.eventIDs[i]
            for j in range(len(person.availabilities[event-1])):
                time = person.availabilities[event-1][j]
                sch.events_avaibilities[event,time].append(person.id)
                if person.id not in sch.persons:
                    sch.persons.append(person.id)

    # print(sch.persons, sch.events_avaibilities)
    return allpeople


a = start()










