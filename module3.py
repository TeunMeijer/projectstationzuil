import psycopg2
import requests
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


# conn = psycopg2.connect(
#     host="localhost",
#     database="zuil",
#     user="postgres",
#     password="gefu.dofuv.07")
# cursor = conn.cursor()
# query = '''SELECT       bericht, date, plaats
#             FROM        bericht
#             WHERE       geldig  = 'true'
#             ORDER BY    id DESC
#             LIMIT       5;'''
#
# cursor.execute(query)
# records = cursor.fetchall()
# conn.close()
#
#
#
#
# for record in records:
#     print(record[0], record[1], record[2])


def denhaag():
    conn = psycopg2.connect(
        host="localhost",
        database="zuil",
        user="postgres",
        password="gefu.dofuv.07")
    cursor = conn.cursor()
    query = '''SELECT       station_city, ov_bike, elevator, toilet, park_and_ride
                FROM        station_service
                WHERE       station_city = 'Den Haag'
                ORDER BY    station_city ASC '''
    cursor.execute(query)
    service = cursor.fetchall()
    conn.close()
    for services in service:
        print(services)

    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=den haag,nl&appid=5d6cab63d757ea8d87737b1f23d0de49&units=metric")
    response_data = r.json()

    for key in response_data.keys():
        print(f"{key}: {response_data[key]}")

    root = Tk()
    denhaag = Label(master=root, text='Den Haag:', height=2, )
    denhaag.pack()

    lift = ImageTk.PhotoImage(Image.open("liftklein.jpg"))

    label4 = tkinter.Label(image=lift)
    label4.image = lift

    label4.place(x=300, y=100)
    root.geometry("900x600")
    root.title("Den Haag")
    root.mainloop()


def haarlem():
    conn = psycopg2.connect(
        host="localhost",
        database="zuil",
        user="postgres",
        password="gefu.dofuv.07")
    cursor = conn.cursor()
    query = '''SELECT       station_city, ov_bike, elevator, toilet, park_and_ride
                FROM        station_service
                WHERE       station_city = 'Haarlem'
                ORDER BY    station_city ASC '''

    cursor.execute(query)
    service = cursor.fetchall()
    conn.close()
    for services in service:
        print(services)

    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=haarlem&appid=5d6cab63d757ea8d87737b1f23d0de49&units=metric")
    response_data = r.json()

    for key in response_data.keys():
        print(f"{key}: {response_data[key]}")
    root = Tk()
    denhaag = Label(master=root, text='Haarlem:', height=2)
    denhaag.pack()
    root.geometry("900x700")
    root.title("Haarlem")


def zaandam():
    conn = psycopg2.connect(
        host="localhost",
        database="zuil",
        user="postgres",
        password="gefu.dofuv.07")
    cursor = conn.cursor()
    query = '''SELECT       station_city, ov_bike, elevator, toilet, park_and_ride
                FROM        station_service
                WHERE       station_city = 'Zaandam'
                ORDER BY    station_city ASC '''

    cursor.execute(query)
    service = cursor.fetchall()
    conn.close()
    for services in service:
        print(services)

    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=zaandam&appid=5d6cab63d757ea8d87737b1f23d0de49&units=metric")
    response_data = r.json()

    for key in response_data.keys():
        print(f"{key}: {response_data[key]}")
    root = Tk()
    denhaag = Label(master=root, text='Zaandam:', height=2)
    denhaag.pack()
    root.geometry("900x700")
    root.title("Zaandam")


stations = open('stations.txt')
station = stations.read()
stations.close()
station = station.split('\n')

root = Tk()

label = Label(master=root, text='Stations:', height=2)
label.pack()

buttonA = Button(master=root, text=station[0], command=denhaag)
buttonA.place(x=40, y=30)

buttonB = Button(master=root, text=station[1], command=haarlem)
buttonB.place(x=120, y=30)

buttonC = Button(master=root, text=station[2], command=zaandam)
buttonC.place(x=200, y=30)

root.geometry("300x200")
root.title("Stations")
root.mainloop()
