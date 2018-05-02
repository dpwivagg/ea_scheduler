import csv
from person import Person
def read_data():
    with open('Refined_data.csv', newline='') as data:
        reader = csv.reader(data)
        next(reader)
        allpeople = {}
        #  Now all people is a dictionary of id and person object. person object does not have id anymore
        for row in reader:
            id = row.pop(0)
            events = [list(map(int, x.split(' '))) for x in row]
            allpeople[id] = Person({}, [], events)

    return allpeople
