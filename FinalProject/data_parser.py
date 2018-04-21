import csv
from FinalProject.person import Person
def read_data():
    with open('Refined_data.csv', newline='') as data:
        reader = csv.reader(data)
        next(reader)

        allpeople = []

        for row in reader:
            id = row.pop(0)
            events = [list(map(int, x.split(' '))) for x in row]
            allpeople.append(Person(id, [], [], events))
        return allpeople

