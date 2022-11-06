ebericht = open("berichten.csv", 'r')

eenbericht = ebericht.read()
eenberichtje = eenbericht.split('\n')
print(eenberichtje[0])
ebericht.close()

del eenberichtje[1]

eebericht = open("berichten.csv", 'w')
eebericht.write("\n".join(eenberichtje))


#with open("berichten.csv", "r") as f:
    #data = f.read().split("\n")

# Remove the 1st line
#del data[1]

# Save the data
#with open("berichten.csv", "w") as f:
   # f.write("\n".join(data))


