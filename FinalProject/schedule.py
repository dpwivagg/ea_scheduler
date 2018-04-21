
class Schedule():
    def __init__(self, persons, events, heuristic):
        self.persons = persons
        self.events = events
        self.heuristic = heuristic


    def cal_heuristic(self):
        heuristic = 0
        for person in self.persons:
            heuristic = heuristic+ person.calc_heuristic()
        for event in self.events:
            heuristic = heuristic + event.calc_heuristic()
        self.heuristic = heuristic



