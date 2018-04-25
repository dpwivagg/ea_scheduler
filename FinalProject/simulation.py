import copy

from FinalProject.person import Person
from FinalProject.event import Event
from FinalProject.shared_constants import *
from FinalProject.data_parser import *
from FinalProject.hillclimbing import *
from FinalProject.genetic import *


allPerson = read_data()
print(allPerson)
# Run Genetic
run_genetic()


# Run hill climb
run_hill_climb()
