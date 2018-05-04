from csv import reader
from person import Person
from event import Event


def read_data():
    with open('Refined_data.csv', newline='') as data:
        allData = reader(data)
        allEvents = {i: Event(i) for i in range(0, len(next(allData)) - 1)}
        allPeople = {}
        for row in allData:
            id = row.pop(0)
            events = [list(map(int, x.split(' '))) for x in row]
            newperson = Person(events)
            for e in newperson.get_available_event_id():
                allEvents[e].add_person_available(id)
            allPeople[id] = newperson
    return allPeople, allEvents
