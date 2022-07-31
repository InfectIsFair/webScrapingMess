import webScraping

def menu():
    print("-----------     Menu Options     -----------\n")
    print("             1) Import Card")
    print("             2) Edit Card")
    print("             3) Remove Card")
    print("             4) Import Card CSV File")
    print("             5) Open Collection GUI")
    print("             6) Quit\n")
    menuOption = input()
    print()

    return menuOption


#checks user input from menu function to make sure it fits the format I need
def menuFormat(menuOpt):
    while True:
        try:
            intCheck = int(menuOpt) + 1
            break
        except:
            menuOpt = input("Please enter an integer:\n")

    while True:
        if int(menuOpt) > 0 and int(menuOpt) < 5:
            break
        else:
            menuOpt = input("Please enter a number in between the menu options:\n")

    return menuOpt


#splits words and capitilises them
def capitaliseWords(funcInput):
    temp = funcInput.lower().split(" ")
    numWords = len(temp)
    counter = 1
    funcInput = ""
    for word in temp:
        word = word.capitalize()
        funcInput += word
        if counter != numWords:
            funcInput += " "
        counter += 1

    return funcInput


#menu option 1, imports singular card
def importCard():

    acceptableTCG = ["MTG", "PTCG"]
    acceptableMTGRarity = ["Common", "Uncommon", "Rare", "Mythic Rare"]
    acceptablePKMNRarity = ["Common", "Uncommon", "Rare", "Promo"]
    acceptableMTGFoilVariance = ["Non Foil", "Foil"]
    acceptablePKMNFoilVariance = ["Non Foil", "Reverse Holo", "Holo"]

    #inputs card tcg, checks if in acceptable tcgs and sets to uppercase
    tcgCheck = "n"

    while tcgCheck.upper() == "N":
        tcg = input("Enter the card's TCG:\n")
        tcg = tcg.upper()
        while tcg not in acceptableTCG:
            tcg = input("Please enter an acceptable Trading Card Game (e.g. ptcg):\n")
            tcg = tcg.upper()
        
        tcgCheck = input("Is " + tcg + " the correct Trading Card Game, respond with Y/N:\n")
        while tcgCheck.upper() not in ["Y", "N"]:
            tcgCheck = input("Please enter an appropriate response:\n")

    #inputs card name, uses capitilise function, and checks if name is correct
    nameCheck = "n"

    while nameCheck.upper() == "N":
        name = input("Enter the card's name:\n")
        name = capitaliseWords(name)

        nameCheck = input("Is " + name + " the correct card name, respond with Y/N:\n")
        while nameCheck.upper() not in ["Y", "N"]:
            nameCheck = input("Please enter an appropriate response:\n")

    #inputs rarity, chooses acceptable rarities based off of tcg
    rarityCheck = "n"

    while rarityCheck.upper() == "N":
        rarity = input("Enter the card's rarity:\n")
        rarity = capitaliseWords(rarity)

        if tcg == "MTG":
            while rarity not in acceptableMTGRarity:
                rarity = input("Please enter a correct rarity for MTG:\n")
                rarity = capitaliseWords(rarity)
        elif tcg == "PTCG":
            while rarity not in acceptablePKMNRarity:
                rarity = input("Please enter a correct rarity for PTCG:\n")
                rarity = capitaliseWords(rarity)

        rarityCheck = input("Is " + rarity + " the correct rarity, respond with Y/N:\n")
        while rarityCheck.upper() not in ["Y", "N"]:
            rarityCheck = input("Please enter an appropriate response:\n")

    #inputs card set, and chooses acceptable formatting based on tcg, checks with user if set is correct
    setCheck = "n"

    while setCheck.upper() == "N":
        set = input("Enter the card's set:\n")

        set = capitaliseWords(set)

        setCheck = input("Is " + set + " the correct card set, respond with Y/N:\n")
        while setCheck.upper() not in ["Y", "N"]:
            setCheck = input("Please enter an appropriate response:\n")

    #inputs card number, as pkmn tcg has multiple set number conventions, so it's unrealistic to format check them, but mtg is simpler in the format of 001
    setNumCheck = "n"

    while setNumCheck.upper() == "N":
        setNum = input("Enter the card's set number:\n")

        if tcg == "MTG":
            while True:
                try:
                    a = int(setNum) + 0
                    if int(setNum) > 0:
                        break
                    else:
                        setNum = input("Please enter a number greater than 0:\n")
                except:
                    setNum = input("Please only enter full numbers:\n")

            lenSetNum = len(setNum)
            temp = ""
            while lenSetNum < 3:
                temp += "0"
                lenSetNum += 1
            
            setNum = temp + setNum
        
        elif tcg == "PTCG":
            setNum = setNum.upper()

        setNumCheck = input("Is " + setNum + " the correct set number, respond with Y/N:\n")
        while setNumCheck.upper() not in ["Y", "N"]:
            setNumCheck = input("Please enter an appropriate response:\n")

    #inputs foil variance, chooses acceptable rarities based off of tcg
    foilCheck = "n"

    while foilCheck.upper() == "N":
        foil = input("Enter the card's foil variance:\n")
        foil = capitaliseWords(foil)

        if tcg == "MTG":
            while foil not in acceptableMTGFoilVariance:
                foil = input("Please enter a correct foil variance for MTG:\n" + str(acceptableMTGFoilVariance) + "\n")
                foil = capitaliseWords(foil)
        elif tcg == "PTCG":
            while foil not in acceptablePKMNFoilVariance:
                foil = input("Please enter a correct foil variance for PTCG:\n" + str(acceptablePKMNFoilVariance) + "\n")
                foil = capitaliseWords(foil)

        foilCheck = input("Is " + foil + " the correct foil variance, respond with Y/N:\n")
        while foilCheck.upper() not in ["Y", "N"]:
            foilCheck = input("Please enter an appropriate response:\n")

    #inputs tcg, mtg has reliable pricing websites (scryfall / magic madhouse), but ptcg needs user input as ebay is the main selling platform
    priceCheck = "n"

    #uses webScraping module to retrieve card image
    imgCheck = "n"

    while imgCheck.upper() == "N":
        image = 0
        if tcg == "MTG":
            image = webScraping.cardImageMTG(name, set)
        
        elif tcg == "PTCG":
            image = webScraping.cardImagePTCG(name, set)

        imgCheck = input("Does the following URL match your card, respond with Y/N:\n" + image + "\n")
        while imgCheck.upper() not in ["Y", "N"]:
            imgCheck = input("Please enter an appropriate response:\n")

    returnList = [tcg, name, rarity, set, setNum, foil, image]
    return returnList


#menuOption = menu()
#menuOption = menuFormat(menuOption)
importCard()
