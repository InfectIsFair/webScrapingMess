import webScraping as main

def ptcgSet2CSV(set, maxNum):    
    for num in range(maxNum):
        funcNum = str(num + 1)
        turing = main.cardDataPTCG(set, funcNum)

        librarian = open('card-library.csv', 'a')

        temp = turing[0]
        turing[0] = main.removePunc(temp)

        count = len(turing)
        for item in turing:

            removeWhitespace = " ".join(item.split())
            librarian.write(removeWhitespace + ",")

            if count == 1:
                librarian.write("\n")
            else:
                librarian.write(" ")
            
            count -= 1

        print(num + 1)


ptcgSet2CSV("STS", 116)
ptcgSet2CSV("EVO", 113)
