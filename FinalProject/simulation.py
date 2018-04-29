import copy

from FinalProject.person import Person
from FinalProject.event import Event
from FinalProject.shared_constants import *
from FinalProject.data_parser import *
from FinalProject.hillclimbing import *
from FinalProject.genetic import *


# allPerson = read_data()
# print(allPerson)
person1 = Person(1,[],{},[])
schedule1 = Schedule(person1,{})
schedule2 = copy.deepcopy(schedule1)
schedule2.persons.id = 5

print(schedule1.persons.id)
print(schedule2.persons.id)
# Run Genetic
# run_genetic()
#
#
# # Run hill climb
# hill_climbing()
