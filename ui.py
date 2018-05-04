from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.image import Image
import pandas as pd
import matplotlib.pyplot as plt
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class MyApp(App):


    def build(self):
        scroller = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root = Accordion(orientation='vertical',size_hint_y=None,height=50*27)
        chart = self.create_gantt()
        for title in chart:
            item = AccordionItem(title=title)
            item.add_widget(Image(source=title))
            root.add_widget(item)

        scroller.add_widget(root)

        return scroller


    def draw_event_schedule(self, a, eventID):
        event_list = []  # 2D [person x schedule]
        event_list.append(["PersonID", "Start", "Finish", "Role"])
        # timeslot = ["8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30"]
        for roles, people in a.events[eventID].roles_filled.items():
            for personID in people:
                time_from = a.persons[personID].availabilities[eventID][0]
                time_to = a.persons[personID].availabilities[eventID][-1] + 1
                # print(personID, time_from, time_to, roles)
                event_list.append([personID, time_from, time_to, roles])
        return event_list

    def create_gantt(self):
        # query event
        for eventNum in range(0,len(self.schedule.events.keys())):
            event = self.draw_event_schedule(self.schedule, eventNum)
            # print(event)
            headers = event.pop(0)
            df = pd.DataFrame(event, columns=headers)
            # print(df)
            #
            df["Diff"] = df.Finish - df.Start
            color = {"PRESENTER": "turquoise", "INTRO": "crimson", "LEAD": "orange", "DEBRIEF": "blue", "NO_ROLE": "grey"}
            fig, ax = plt.subplots()#figsize=df.shape)
            labels = []
            for i, person in enumerate(df.groupby("PersonID")):
                labels.append(person[0])
                for r in person[1].groupby("Role"):
                    data = r[1][["Start", "Diff"]]
                    ax.broken_barh(data.values, (i - 0.4, 0.8), color=color[r[0]])

            ax.set_xticklabels([" ", "8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30"])
            ax.set_yticks(range(len(labels)))
            ax.set_yticklabels(labels)
            ax.set_ylabel("PersonID")
            ax.set_xlabel("Schedule for Event" + str(eventNum + 1))
            # plt.tight_layout()
            # plt.show()
            # fig.savefig(title)
            # fig = plt.figure()
            title = 'img/Event' + str(eventNum) + '.png'
            fig.savefig(title)
            yield title