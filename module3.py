import psycopg2
import requests
from tkinter import *
from PIL import Image, ImageTk
import tkinter

conn = psycopg2.connect(
    host="localhost",
    database="zuil",
    user="postgres",
    password="gefu.dofuv.07")
cursor = conn.cursor()
query = '''SELECT       bericht, date, plaats
            FROM        bericht
            WHERE       geldig  = 'true'
            ORDER BY    id DESC
            LIMIT       5;'''

cursor.execute(query)
records = cursor.fetchall()
conn.close()

bericht0 = records[0]
bericht1 = records[1]
bericht2 = records[2]
bericht3 = records[3]
bericht4 = records[4]

eenbericht0 = ('het bericht: {}\nDatum: {}\nStation: {}'.format(bericht0[0], bericht0[1], bericht0[2]))
eenbericht1 = ('het bericht: {}\nDatum: {}\nStation: {}'.format(bericht1[0], bericht1[1], bericht1[2]))
eenbericht2 = ('het bericht: {}\nDatum: {}\nStation: {}'.format(bericht2[0], bericht2[1], bericht2[2]))
eenbericht3 = ('het bericht: {}\nDatum: {}\nStation: {}'.format(bericht3[0], bericht3[1], bericht3[2]))
eenbericht4 = ('het bericht: {}\nDatum: {}\nStation: {}'.format(bericht4[0], bericht4[1], bericht4[2]))


def denhaag():
    label.destroy()
    buttonA.destroy()
    buttonB.destroy()
    buttonC.destroy()

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
    services = str(service)
    servies = services.split(',')

    ovfiets = servies[1]
    lift = servies[2]
    toilet = servies[3]
    parkeerplaats = servies[4]

    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=den haag,nl&appid=5d6cab63d757ea8d87737b1f23d0de49&units=metric")
    json = r.json()
    temp = json['main']['temp']
    weer = json['weather'][0]['main']
    final = (temp, weer)

    tempra = Label(root, text='tempratuur', font=(30))
    tempra.place(x=30, y=100)
    weerbuiten = Label(root, text='weer', font=(30))
    weerbuiten.place(x=30, y=200)
    tempra['text'] = '{}C'.format(final[0])
    weerbuiten['text'] = final[1]

    denhaag = Label(master=root, text='Welkom op station Den Haag:', font=(20), height=2)
    denhaag.pack()

    if 'True' in ovfiets:
        fiets = ImageTk.PhotoImage(Image.open("img_ovfiets.png"))
        label1 = Label(image=fiets)
        label1.image = fiets
        label1.pack(side=LEFT, anchor="s")

    if 'True' in lift:
        lift1 = ImageTk.PhotoImage(Image.open("liftklein.jpg"))
        label2 = Label(image=lift1)
        label2.image = lift1
        label2.pack(side=LEFT, anchor="s")
    if 'True' in toilet:
        wc = ImageTk.PhotoImage(Image.open("img_toilet.png"))
        label3 = Label(image=wc)
        label3.image = wc
        label3.pack(side=LEFT, anchor="s")
    if 'True' in parkeerplaats:
        pr = ImageTk.PhotoImage(Image.open("img_pr.png"))
        label4 = Label(image=pr)
        label4.image = pr
        label4.pack(side=LEFT, anchor="s")

    berichtje1 = Label(master=root, text=eenbericht0, height=4)
    berichtje1.pack(ipadx=10, ipady=10, anchor="e")
    berichtje2 = Label(master=root, text=eenbericht1, height=4)
    berichtje2.pack(ipadx=10, ipady=10, anchor="e")
    berichtje3 = Label(master=root, text=eenbericht2, height=4)
    berichtje3.pack(ipadx=10, ipady=10, anchor="e")
    berichtje4 = Label(master=root, text=eenbericht3, height=4)
    berichtje4.pack(ipadx=10, ipady=10, anchor="e")
    berichtje5 = Label(master=root, text=eenbericht4, height=4)
    berichtje5.pack(ipadx=10, ipady=10, anchor="e")

    facaliteiten = Label(master=root, text='De facaliteiten op dit station:', font=(14), height=1)
    facaliteiten.place(x=0, y=475)


def haarlem():
    label.destroy()
    buttonA.destroy()
    buttonB.destroy()
    buttonC.destroy()

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
    services = str(service)
    servies = services.split(',')

    ovfiets = servies[1]
    lift = servies[2]
    toilet = servies[3]
    parkeerplaats = servies[4]

    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=haarlem&appid=5d6cab63d757ea8d87737b1f23d0de49&units=metric")
    json = r.json()

    temp = json['main']['temp']
    weer = json['weather'][0]['main']
    final = (temp, weer)

    tempra = Label(root, text='tempratuur', font=(30))
    tempra.place(x=30, y=100)
    weerbuiten = Label(root, text='weer', font=(30))
    weerbuiten.place(x=30, y=200)
    tempra['text'] = '{}C'.format(final[0])
    weerbuiten['text'] = final[1]

    denhaag = Label(master=root, text='Welkom op station Haarlem:', font=(40), height=2)
    denhaag.pack()

    if 'True' in ovfiets:
        fiets = ImageTk.PhotoImage(Image.open("img_ovfiets.png"))
        label1 = Label(image=fiets)
        label1.image = fiets
        label1.pack(side=LEFT, anchor="s")

    if 'True' in lift:
        lift1 = ImageTk.PhotoImage(Image.open("liftklein.jpg"))
        label2 = Label(image=lift1)
        label2.image = lift1
        label2.pack(side=LEFT, anchor="s")
    if 'True' in toilet:
        wc = ImageTk.PhotoImage(Image.open("img_toilet.png"))
        label3 = Label(image=wc)
        label3.image = wc
        label3.pack(side=LEFT, anchor="s")
    if 'True' in parkeerplaats:
        pr = ImageTk.PhotoImage(Image.open("img_pr.png"))
        label4 = Label(image=pr)
        label4.image = pr
        label4.pack(side=LEFT, anchor="s")

    berichtje1 = Label(master=root, text=eenbericht0, height=4)
    berichtje1.pack(ipadx=10, ipady=10, anchor="e")
    berichtje2 = Label(master=root, text=eenbericht1, height=4)
    berichtje2.pack(ipadx=10, ipady=10, anchor="e")
    berichtje3 = Label(master=root, text=eenbericht2, height=4)
    berichtje3.pack(ipadx=10, ipady=10, anchor="e")
    berichtje4 = Label(master=root, text=eenbericht3, height=4)
    berichtje4.pack(ipadx=10, ipady=10, anchor="e")
    berichtje5 = Label(master=root, text=eenbericht4, height=4)
    berichtje5.pack(ipadx=10, ipady=10, anchor="e")

    facaliteiten = Label(master=root, text='De facaliteiten op dit station:', font=(14), height=1)
    facaliteiten.place(x=0, y=475)


def zaandam():
    label.destroy()
    buttonA.destroy()
    buttonB.destroy()
    buttonC.destroy()

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
    services = str(service)
    servies = services.split(',')

    ovfiets = servies[1]
    lift = servies[2]
    toilet = servies[3]
    parkeerplaats = servies[4]

    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=zaandam&appid=5d6cab63d757ea8d87737b1f23d0de49&units=metric")
    json = r.json()

    temp = json['main']['temp']
    weer = json['weather'][0]['main']
    final = (temp, weer)

    denhaag = Label(master=root, text='Welkom op station Zaandam:', font=(20), height=2)
    denhaag.pack()

    if 'True' in ovfiets:
        fiets = ImageTk.PhotoImage(Image.open("img_ovfiets.png"))
        label1 = Label(image=fiets)
        label1.image = fiets
        label1.pack(side=LEFT, anchor="s")

    if 'True' in lift:
        lift1 = ImageTk.PhotoImage(Image.open("liftklein.jpg"))
        label2 = Label(image=lift1)
        label2.image = lift1
        label2.pack(side=LEFT, anchor="s")
    if 'True' in toilet:
        wc = ImageTk.PhotoImage(Image.open("img_toilet.png"))
        label3 = Label(image=wc)
        label3.image = wc
        label3.pack(side=LEFT, anchor="s")
    if 'True' in parkeerplaats:
        pr = ImageTk.PhotoImage(Image.open("img_pr.png"))
        label4 = Label(image=pr)
        label4.image = pr
        label4.pack(side=LEFT, anchor="s")

    berichtje1 = Label(master=root, text=eenbericht0, height=4)
    berichtje1.pack(ipadx=10, ipady=10, anchor="e")
    berichtje2 = Label(master=root, text=eenbericht1, height=4)
    berichtje2.pack(ipadx=10, ipady=10, anchor="e")
    berichtje3 = Label(master=root, text=eenbericht2, height=4)
    berichtje3.pack(ipadx=10, ipady=10, anchor="e")
    berichtje4 = Label(master=root, text=eenbericht3, height=4)
    berichtje4.pack(ipadx=10, ipady=10, anchor="e")
    berichtje5 = Label(master=root, text=eenbericht4, height=4)
    berichtje5.pack(ipadx=10, ipady=10, anchor="e")

    tempra = Label(root, text='tempratuur', font=(30))
    tempra.place(x=30, y=100)
    weerbuiten = Label(root, text='weer', font=(30))
    weerbuiten.place(x=30, y=200)
    tempra['text'] = '{}C'.format(final[0])
    weerbuiten['text'] = final[1]

    facaliteiten = Label(master=root, text='De facaliteiten op dit station:', font=(14), height=1)
    facaliteiten.place(x=0, y=475)


stations = open('stations.txt')
station = stations.read()
stations.close()
station = station.split('\n')

root = tkinter.Tk()

label = Label(master=root, font=(20), text='Stations:', height=2)
label.pack(padx=10, pady=10)

buttonA = Button(master=root, font=(16), text=station[0], relief=RAISED, command=denhaag)
buttonA.pack(ipadx=10, ipady=10)

buttonB = Button(master=root, font=(16), text=station[1], relief=RAISED, command=haarlem)
buttonB.pack(ipadx=10, ipady=10)

buttonC = Button(master=root, font=(16), text=station[2], relief=RAISED, command=zaandam)
buttonC.pack(ipadx=10, ipady=10)

root.geometry("900x600")
root.title("Stations")
root.mainloop()
