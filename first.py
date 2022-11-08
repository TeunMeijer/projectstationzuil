import datetime
import random

bericht = input('wat wil je zeggen: ') # bericht ingeven
beriecht = bericht.replace(',', 'ß') # de comma veranderen in een ander teken anders verkeerd lezen
while len(beriecht) > 140: # als bericht langer is dan 140 carakters
    print('uw bericht is te lang u kan maximaal 140 caracters gebruiken')
    bericht = input('wat wil je zeggen: ') # laat ze het bericht nog een keer invoeren
    beriecht = bericht.replace('ß', ',')
datumtijd = datetime.datetime.today() # maak de tijd aan
datum = str(datumtijd.strftime("%a %d %b %Y")) # de datum
tijd = str(datumtijd.strftime("%X")) # de tijd
naam = input("wat is je naam: ")# vraag om de naam
if naam == '': # als naam niks is
    naam = 'anoniem' # word naam annoniem
stations = open('stations.txt') # open het bestand met de stations
station = stations.readlines()  #lees de stations
stations.close() # sluit het bestand met de stations
randstation = random.choice(station)    #kies een random station

berichten = open('berichten.csv', 'a')  #open het csv bestand
print('Bericht: {} \nDatum en tijd: {}: {} \nNaam: {} \nStation: {}'
      .format(bericht, datum, tijd, naam, randstation))

berichten.write('{}, {}, {}, {}, {}'.format(beriecht, datum, tijd, naam, randstation)) # zet alle gegevens in een csv bestand
berichten.close() # sluit het csv bestand



