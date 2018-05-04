from data_parser import read_data
from makeschedule import makeschedule
from ui import MyApp

allPeople, allEvents = read_data()
schedule = makeschedule(allPeople, allEvents, 300)
print("Final result: ", schedule)
schedule.check_correct()

new_window = MyApp()
new_window.schedule = schedule
new_window.run()
