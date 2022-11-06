import datetime
import random

bericht = input('wat wil je zeggen: ')
while len(bericht) > 140:
    print('uw bericht is te lang u kan maximaal 140 caracters gebruiken')
    bericht = input('wat wil je zeggen: ')
datumtijd = datetime.datetime.today()
datum = str(datumtijd.strftime("%a %d %b %Y"))
tijd = str(datumtijd.strftime("%X"))
naam = input("wat is je naam: ")
if naam == '':
    naam = 'anoniem'
stations = open('stations.txt')
station = stations.readlines()
stations.close()
randstation = random.choice(station)

berichten = open('berichten.csv', 'a')
print('Bericht: {} \nDatum en tijd: {}: {} \nNaam: {} \nStation: {}'
      .format(bericht, datum, tijd, naam, randstation))

berichten.write('{}, {}, {}, {}, {}'.format(bericht, datum, tijd, naam, randstation))
berichten.close()
