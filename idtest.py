ebericht = open("berichten.csv", 'r')

eenbericht = ebericht.read()
eenberichtje = eenbericht.split('\n')
print(eenberichtje[0])
ebericht.close()

del eenberichtje[1]

eebericht = open("berichten.csv", 'w')
eebericht.write("\n".join(eenberichtje))

