import datetime
import psycopg2

hetid = open("id.txt")
eenid = hetid.readlines()
hetid.close()
id = int(eenid[-1]) + 1
geschrevenid = (str(id) + '\n')

deid = open('id.txt', 'a')
deid.write(geschrevenid)
deid.close()

datumtijd = datetime.datetime.today()
datumbeoordeling = str(datumtijd.strftime("%a %d %b %Y"))
tijdbeoordeling = str(datumtijd.strftime("%X"))

berichten = open("berichten.csv")
bericht = berichten.readline()
berichtjes = bericht.split(',')
hetbericht = berichtjes[0]
datum = berichtjes[1]
tijd = berichtjes[2]
naam = berichtjes[3]
plaats = berichtjes[4]
berichten.close()
if 'ß' in hetbericht:
    bericht.replace('ß', ',')

print('het bericht: {} \ndatum en tijd: {},{} \nnaam: {} \nstation: {}'.format(hetbericht, datum, tijd, naam, plaats))
goedgekeurd = bool(input('goedgekeurd(als hij fout is vul niks in anders vul iets in): '))
naammoderator = input('naam: ')
email = input('email: ')
print(
    'het bericht: {} \ndatum en tijd: {},{} \nnaam: {} \nstation: {}goedgekeurd: {} \ndatum en tijd beoordeling: {}, {} \n'
    'naam en emailadres beoordeler: {} ,{}'
    .format(hetbericht, datum, tijd, naam, plaats, goedgekeurd, datumbeoordeling, tijdbeoordeling, naammoderator,
            email))


conn = psycopg2.connect(
    host="localhost",
    database="zuil",
    user="postgres",
    password="gefu.dofuv.07")

cursor = conn.cursor()
query = """INSERT INTO bericht (id, bericht, date, time, naam, plaats , geldig, datumbeoordeling, tijdbeoordeling, naammoderator, emailmoderator)
            VALUES (%s ,%s ,%s ,%s  ,%s ,%s ,%s, %s, %s,%s,%s  );"""

data = (id, hetbericht, datum, tijd, naam, plaats, goedgekeurd, datumbeoordeling, tijdbeoordeling, naammoderator, email)
cursor.execute(query, data)

conn.commit()
conn.close()

ebericht = open("berichten.csv", 'r')

eenbericht = ebericht.read()
eenberichtje = eenbericht.split('\n')
print(eenberichtje[0])
ebericht.close()

del eenberichtje[1]

eebericht = open("berichten.csv", 'w')
eebericht.write("\n".join(eenberichtje))
