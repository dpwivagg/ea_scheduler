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

for id, event in allEvents.items():
    print("Event Id ", id, " ", event.available_persons)


# Run Genetic


