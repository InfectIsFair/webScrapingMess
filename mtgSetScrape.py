import webScraping as main

def mtgSet2CSV(set, maxNum):    
    for num in range(maxNum):
        funcNum = str(num + 1)
        turing = main.cardDataMTG(set, funcNum)

        librarian = open('card-library.csv', 'a')

        librarian.write("MTG, ")

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


mtgSet2CSV('NEO', 512)
