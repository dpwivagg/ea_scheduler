import copy

from FinalProject.person import Person
from FinalProject.event import Event
from FinalProject.schedule import Schedule
from FinalProject.shared_constants import *
from FinalProject.data_parser import *
# from FinalProject.hillclimbing import *
from FinalProject.genetic import *


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

original_copy = copy.deepcopy(schedule)

# print(original_copy.persons['1000'].availabilities)

# random start
def start(original_copy):
    persons = copy.deepcopy(original_copy.persons)
    events = copy.deepcopy(original_copy.events)
    role_list = ["PRESENTER","INTRO","LEAD","DEBRIEF", "NO_ROLE"]
    for personID in persons.keys():
        available_events = persons[personID].get_available_event_id()
        print(str(personID))
        print(available_events)
        randomNum = random.randint(1,int(len(available_events)))
        # randomSample = [ available_events[i] for i in sorted(random.sample(available_events), 4))]
        persons[personID].eventIDs = random.sample(available_events, randomNum)
        persons[personID].eventIDs.sort()
        print(randomNum)
        print(persons[personID].eventIDs)
        # print(persons[personID].eventIDs)

        for item in persons[personID].eventIDs:
            x = random.randint(0, 4)
            persons[personID].roles[role_list[x]] += 1
            events[item].roles_filled[role_list[x]].append(personID)
            events[item].available_persons.remove(personID)

    # for i in events.keys():
    #     print(str(i) + str(events[i].roles_filled))
    #     print(str(i) + str(events[i].available_persons))
    #
    # for i in persons.keys():
    #     print(str(persons[i].eventIDs))
    #     print(str(persons[i].roles))

    return Schedule(persons,events)



start(original_copy)


# for id, event in allEvents.items():
#     print("Event Id ", id, " ", event.available_persons)

# for id, event in allEvents.items():
#     print("Event Id ", id, " ", event.available_persons)


# Run Genetic


