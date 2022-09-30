from sqlalchemy import null
import webScraping as main

def ptcgSet2CSV(set, maxNum):
    cardBeforeTG = None
    for num in range(maxNum):
        funcNum = str(num + 1)
        try:
            try:
                turing = main.cardDataPTCG(set, funcNum)
            except:
                if cardBeforeTG == None:
                    cardBeforeTG = num
                turing = main.cardDataPTCGVariants(set, num+1, cardBeforeTG)
        except:
            try:
                turing = main.cardDataPTCG(set, "G")
            except:
                print("error located at " + set + str(num+1))
                break

        if turing[0] != "error":
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
        else:
            print("Error found at " + set + " " + str(num+1))


# card variants: RC SV TG a etc.

# energy
