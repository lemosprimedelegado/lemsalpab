with open("C:/Users/2026158215/Documents/catatoide.txt", "r") as gff:
    for line in gff:
        line = line.strip() #remove newline character at end of each line
        phrase = line.split()
        newDict = {phrase[0]: (phrase[1], phrase[2], phrase[3], phrase[4], phrase[5], phrase[6], phrase[7], phrase[8], phrase[9], phrase[10]) }
        print(newDict)


