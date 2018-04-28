import copy

from FinalProject.person import Person
from FinalProject.event import Event
from FinalProject.shared_constants import *
from FinalProject.data_parser import *
from FinalProject.hillclimbing import *
from FinalProject.genetic import *


allPerson = read_data()
allAvailability = {}
for i in range(0,7):        # time slot identifiers 0-6
    for j in range(1,22):   # event identifiers 1-21
        allAvailability[j,i] = []


print(allPerson)
a = Schedule(allPerson, allAvailability)
b,s = a.form_possible_schedules()
# Run Genetic
# run_genetic()
#
#
# # Run hill climb
# run_hill_climb()
