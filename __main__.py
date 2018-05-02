import copy

from person import Person
from event import Event
from schedule import Schedule
from shared_constants import *
from data_parser import *
from makeschedule import makeschedule

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

a = makeschedule(allPeople, allEvents, 600)
print("Final result: ", a)
a.check_correct()

# plot schedule for each event in Gantt
import pandas as pd
import io
import matplotlib.pyplot as plt

def draw_event_schedule(a, eventID):
    event_list = [] # 2D [person x schedule]
    event_list.append(["PersonID", "Start", "Finish", "Role"])
    # timeslot = ["8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30"]
    for roles in a.events[eventID].roles_filled.keys():
        for personID in a.events[eventID].roles_filled[roles]:
            time_from = a.persons[personID].availabilities[eventID][0]
            time_to = a.persons[personID].availabilities[eventID][-1] + 1
            print(personID, time_from, time_to, roles)
            event_list.append([personID, time_from, time_to, roles])
    return event_list

# query event
eventNum = 0
event = draw_event_schedule(a, eventNum)
headers = event.pop(0)
df = pd.DataFrame(event, columns=headers)
print(df)


df["Diff"] = df.Finish - df.Start
color = {"PRESENTER":"turquoise", "INTRO":"crimson", "LEAD":"orange", "DEBRIEF":"blue", "NO_ROLE":"grey"}
fig,ax=plt.subplots(figsize=df.shape)
labels=[]
for i, person in enumerate(df.groupby("PersonID")):
    labels.append(person[0])
    for r in person[1].groupby("Role"):
        data = r[1][["Start", "Diff"]]
        ax.broken_barh(data.values, (i-0.4,0.8), color=color[r[0]] )

ax.set_xticklabels([" ", "8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30"])
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels)
ax.set_ylabel("PersonID")
ax.set_xlabel("Schedule for Event" + str(eventNum + 1))
plt.tight_layout()
plt.show()
