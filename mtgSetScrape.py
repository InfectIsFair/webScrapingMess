import webScraping as main

def mtgSet2CSV(set, maxNum):    
    for num in range(maxNum):
        funcNum = str(num + 1)
        turing = main.cardDataMTG(set, funcNum)

        librarian = open('card-library.csv', 'a')

        temp = turing[0]
        turing[0] = main.removePunc(temp)

        count = len(turing)
        for item in turing:

            removeWhitespace = " ".join(item.split())
            librarian.write(removeWhitespace + ",")

            if count == 1:
                librarian.write("\n")
            
            count -= 1

        print(num + 1)

# alchemy sucks

# Japanese cards
# mtgSet2CSV("WAR", 312)

# flip cards
# Uvilda & Nassari

# card variations (rules txt for starter decks)
# mtgSet2CSV("KLD", 278)
# mtgSet2CSV("AER", 197)

# strict proctor variant
# mtgSet2CSV("STX", 394)
