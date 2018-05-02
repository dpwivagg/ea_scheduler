import copy

from hillclimbing import Hill_Climb
from person import Person
from event import Event
from schedule import Schedule
from shared_constants import *
from data_parser import *

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


hill_climb = Hill_Climb(original_copy)
a = hill_climb.hill_climbing()
print("Final result: ", a)
a.check_correct()