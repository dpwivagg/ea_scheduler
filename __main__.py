import copy

from person import Person
from event import Event
from schedule import Schedule
from shared_constants import *
from data_parser import *
from makeschedule import makeschedule
from ui import MyApp

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

a = makeschedule(allPeople, allEvents, 3)
print("Final result: ", a)
a.check_correct()


new_window = MyApp()
new_window.schedule = schedule
new_window.run()