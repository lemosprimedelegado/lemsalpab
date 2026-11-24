with open("C:/Users/2026158215/Documents/txt.txt", "r") as gff:
    for line in gff:
        print(line.strip())


    infile = open("C:/Users/2026158215/Documents/txt.txt", "r")

    for line in infile:
        line = line.strip() #remove newline character at end of each line
        phrase = line.split()
        newDict = {phrase[0]: (phrase[1], phrase[2])}
        print(newDict)


#miau = open("updatedlist.txt", "x")
gato = open("updatedlist.txt", "a")
gato.write("Tunisia	36.9500	8.8500" + "\nVar     43.1333 6.2500")
gato = open ("updatedlist.txt", "r")
print(gato.read())

cao = open("updatedlist.txt", "r")
for line in cao:
        line = line.strip() #remove newline character at end of each line
        phrase = line.split()
        newDict2 = {phrase[0]: (phrase[1], phrase[2])}
        print(newDict2)

