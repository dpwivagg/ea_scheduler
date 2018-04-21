import copy

from FinalProject.person import Person
from FinalProject.event import Event
from FinalProject.shared_constants import *

id = 1
event1 = Event(id,None)
person1 = Person(11,lead,event1,None)

event2 = copy.deepcopy(event1)
person2 = copy.deepcopy(person1)

event2.id = 2

print("Person2 Event ", person2.events.id)
print("Person1 Event ", person1.events.id)