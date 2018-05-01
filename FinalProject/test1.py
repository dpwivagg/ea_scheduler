from FinalProject.schedule import Schedule
from FinalProject.data_parser import read_data
from FinalProject.event import Event
from FinalProject.hillclimbing import Hill_Climb
from copy import deepcopy

# allPeople = read_data()
#
# #  Create events
# allEvents = {}
# for i in range(0,21):
#     event = Event(i,{})
#     allEvents[i] = event
#
# for id ,person in allPeople.items():
#     available_events = person.get_available_event_id()
#     for event_id in available_events:
#         allEvents[event_id].add_person_available(id)
#
# schedule = Schedule(allPeople, allEvents)
#
# heuristic = 0

allPeople = read_data()

#  Create events
allEvents = {}
for i in range(0,21):
    event = Event(i,{})
    allEvents[i] = event

for id ,person in allPeople.items():
    available_events = person.get_available_event_id()
    for event_id in available_events:
        allEvents[event_id].add_person_available(id)

schedule = Schedule(allPeople, allEvents)

original_copy = deepcopy(schedule)

hill_climb = Hill_Climb(original_copy)
schedule = hill_climb.hill_climbing()

for i in schedule.persons.keys():
    print(str(i)+ '\t' + str(schedule.persons[i].eventIDs))

print("!!!!!")

h = 0

for eventID in schedule.events.keys():
    timeslot = {}
    count = 0
    for personID in schedule.persons.keys():
        if eventID in schedule.persons[personID].eventIDs:
            for time in schedule.persons[personID].availabilities[eventID]:
                if time not in timeslot.keys():
                    timeslot[time] = [personID]
                else:
                    timeslot[time].append(personID)
    print(str(eventID) + '\t' + str(timeslot))
    for i in timeslot.keys():
        if i in [2, 3, 4, 5]:
            Num = len(timeslot[i])
            if Num >= 4 and Num <= 7:
                count += 1
    if count < 4:
        h -= 5
    else:
        h += 1
    count = 0

    print(h)


