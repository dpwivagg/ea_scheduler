import copy

from FinalProject.hillclimbing import Hill_Climb
from FinalProject.person import Person
from FinalProject.event import Event
from FinalProject.schedule import Schedule
from FinalProject.shared_constants import *
from FinalProject.data_parser import *
# from FinalProject.hillclimbing import *
from FinalProject.genetic import *
from copy import deepcopy


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




# schedule1 = start(schedule)
# schedule2 = start(schedule)
# children1, children2 = schedule1.cross_over(schedule2, original_copy)
#
# print("Schedule1 ", "Event 0 Role", str(schedule1.events[0].roles_filled))
# print("Schedule1 ", "Event 0 Persons", str(schedule1.events[0].available_persons))
#
# print("Child1 ", "Event 0 Role", str(children1.events[0].roles_filled))
# print("Child1 ", "Event 0 Persons", str(children1.events[0].available_persons))
#
# print("Schedule2 ", "Event 0 Role", str(schedule2.events[0].roles_filled))
# print("Schedule2 ", "Event 0 Persons", str(schedule2.events[0].available_persons))
#
#
#
# print("Child2 ", "Event 0 Role", str(children2.events[0].roles_filled))
# print("Child2 ", "Event 0 Persons", str(children2.events[0].available_persons))



<<<<<<< HEAD
# hill_climb = Hill_Climb(original_copy)
# hill_climb.hill_climbing(schedule)
run_genetic(original_copy)
=======
schedule1 = start(schedule)
schedule2 = start(schedule)
children1, children2 = schedule1.cross_over(schedule2, original_copy)

print("Schedule1 ", "Event 0 Role", str(schedule1.events[0].roles_filled))
print("Schedule1 ", "Event 0 Persons", str(schedule1.events[0].available_persons))

print("Child1 ", "Event 0 Role", str(children1.events[0].roles_filled))
print("Child1 ", "Event 0 Persons", str(children1.events[0].available_persons))

print("Schedule2 ", "Event 0 Role", str(schedule2.events[0].roles_filled))
print("Schedule2 ", "Event 0 Persons", str(schedule2.events[0].available_persons))



print("Child2 ", "Event 0 Role", str(children2.events[0].roles_filled))
print("Child2 ", "Event 0 Persons", str(children2.events[0].available_persons))



hill_climb = Hill_Climb(original_copy)
hill_climb.hill_climbing()
>>>>>>> 23e677ffd1cf1d8f028e642024491b61b169d81f
# for id, event in allEvents.items():
#     print("Event Id ", id, " ", event.available_persons)

# for id, event in allEvents.items():
#     print("Event Id ", id, " ", event.available_persons)


# Run Genetic


