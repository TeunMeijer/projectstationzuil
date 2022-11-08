import datetime
import psycopg2

hetid = open("id.txt") # open het bestand met de id's
eenid = hetid.readlines() # lees alle id's
hetid.close() #sluit het bestand met de id's
id = int(eenid[-1]) + 1 # tel er 1 op bij het laatste nummer van het bestand met de id's
geschrevenid = (str(id) + '\n')  #zet het nieuwe nummer in het bestand met de id's

deid = open('id.txt', 'a') #open het bestand met de id's om er een nieuwe achteraan te schrijven
deid.write(geschrevenid)    #zet het nieuwe nummer in het bestand met de id's
deid.close() # sluit het bstand met het nieuwe nummer

datumtijd = datetime.datetime.today() # maak de tijd aan
datumbeoordeling = str(datumtijd.strftime("%a %d %b %Y")) # de datum
tijdbeoordeling = str(datumtijd.strftime("%X")) # de tijd

berichten = open("berichten.csv") #open het bestand met de berichten
bericht = berichten.readline() #lees de eerste regel van het bestand
berichtjes = bericht.split(',')# splits de regel op de comma
hetberichte = berichtjes[0]
datum = berichtjes[1]
tijd = berichtjes[2]
naam = berichtjes[3]
plaats = berichtjes[4]
berichten.close()# sluit het bestand met het bericht
hetbericht = hetberichte.replace('ß', ',') #verander in het bericht het teken naar een comma

print('het bericht: {} \ndatum en tijd: {},{} \nnaam: {} \nstation: {}'.format(hetbericht, datum, tijd, naam, plaats)) #print het bericht
goedgekeurd = bool(input('goedgekeurd(als hij fout is vul niks in anders vul iets in): '))# keur het bericht goed of four
naammoderator = input('naam: ')# voer de naam van de moderator toe
email = input('email: ')# voer het e-mailadres van de moderator toe
print(
    'het bericht: {} \ndatum en tijd: {},{} \nnaam: {} \nstation: {}goedgekeurd: {} \ndatum en tijd beoordeling: {}, {} \n'
    'naam en emailadres beoordeler: {} ,{}'
    .format(hetbericht, datum, tijd, naam, plaats, goedgekeurd, datumbeoordeling, tijdbeoordeling, naammoderator,
            email))# print het hele bericht


ebericht = open("berichten.csv", 'r') # open het bestand van de berichten

eenbericht = ebericht.read() # en lees het
eenberichtje = eenbericht.split('\n')  # splits het bestand op de enter
ebericht.close()# sluit het bestand

del eenberichtje[0] # verwijder de eerste regel

eebericht = open("berichten.csv", 'w') # open het bestand opnieuw
eebericht.write("\n".join(eenberichtje))# schrijf alles in het bestand behalve de verwijderde regel

conn = psycopg2.connect(
    host="localhost",
    database="zuil",
    user="postgres",
    password="gefu.dofuv.07") # connect met de database

cursor = conn.cursor()
query = """INSERT INTO bericht (id, bericht, date, time, naam, plaats , geldig, datumbeoordeling, tijdbeoordeling, naammoderator, emailmoderator)
            VALUES (%s ,%s ,%s ,%s  ,%s ,%s ,%s, %s, %s,%s,%s  );""" # zet de berichten in de database

data = (id, hetbericht, datum, tijd, naam, plaats, goedgekeurd, datumbeoordeling, tijdbeoordeling, naammoderator, email)
cursor.execute(query, data) #voeg de querty en de data samen

conn.commit() # verstuur het naar de database
conn.close() #sluit de connectie met de database


