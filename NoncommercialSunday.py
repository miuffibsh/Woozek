import tkinter as tki
import datetime
from win10toast import ToastNotifier


class NoncommercialSunday:

    def __init__(self, master):
        toast = ToastNotifier()
        reminder_date = ["12/12/2022", "19/12/2022", "30/01/2023", "03/04/2023", "01/05/2023", "26/06/2023",
                         "28/08/2023", "18/12/2023", "25/12/2023"]

        for day in reminder_date:
            time_delta = datetime.datetime.strptime(day, "%d/%m/%Y") - datetime.datetime.now()
            if 0 <= time_delta.days < 7:
                label = tki.Label(master, text="The sunday this week is commercial", font=("Century Gothic", 9),
                                  bg='#e3d5ca')
                label.pack()
                toast.show_toast("Woozek", "Commercial Sunday", duration=20, threaded=True)
                break
            elif time_delta.days >= 0:
                label = tki.Label(master, text="The sunday this week is non-commercial", font=("Century Gothic", 9),
                                  bg='#e3d5ca')
                toast.show_toast("Woozek", "Non-commercial Sunday", duration=20, threaded=True)
                label.pack()
                break
