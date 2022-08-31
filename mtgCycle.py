import main

def mtgSet2CSV(set, maxNum):    
    for num in range(maxNum):
        funcNum = str(num + 1)
        turing = main.cardDataMTG(set, funcNum)

        librarian = open('card-library.csv', 'a')

        count = len(turing)
        for item in turing:

            librarian.write("MTG, ")

            removeWhitespace = " ".join(item.split())
            librarian.write(removeWhitespace + ",")

            if count == 1:
                librarian.write("\n")
            else:
                librarian.write(" ")
            
            count -= 1

        print(num + 1)


mtgSet2CSV('XLN', 10)
