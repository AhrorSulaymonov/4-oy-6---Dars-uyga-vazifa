from os import system
from datetime import datetime , date
system("cls")
class Time:
    def __init__(self, hour : int, minut : int, sekund : int) -> None:
        self.hour = hour
        self.minut = minut
        self.sekund = sekund
    def __str__(self) -> str:
        return f"{self.hour}:{self.minut}:{self.sekund}"
class TimeTable(Time):
    def __init__(self,subject : str, startTime : Time, classroom : str) -> None:
        self.subject = subject
        self.startTime =  startTime
        self.classroom = classroom
    def info(self):
        return f"""
    Fan : {self.subject}
    Boshlanish vaqti : {self.startTime}
    Auditoriya : {self.classroom}
"""

timetables = []
timetables.append(TimeTable("Oliy matematika",Time(14,30,00),"A120"))
timetables.append(TimeTable("Diskret matematika",Time(16,00,00),"A124"))
timetables.append(TimeTable("Ehtimollar nazariyasi",Time(17,30,00),"A220"))
timetables.append(TimeTable("Ingliz tili",Time(19,00,00),"A120"))
timetables.append(TimeTable("Matematik analiz",Time(20,30,00),"A420"))
time = input("iltimos vaqt kiriting (EX: hh:mm:ss): ")
time = time.split(":")
for i in timetables:
    if i.startTime.hour == int(time[0]) and i.startTime.minut == int(time[1])  and i.startTime.sekund == int(time[2]):
        print(i.info())
print(date.today())