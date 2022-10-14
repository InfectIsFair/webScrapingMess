from flask import Flask, render_template, url_for
import orderSetCSVByDate
import sqlCreateDb

def importCSV():
    returnList = []
    librarian = open('card-library.csv', 'r')
    for line in librarian.readlines():
        returnList.append(line.split(','))

    return returnList


def importSetCSV():
    returnList = []
    librarian = open("mtg-set.csv", "r")
    for line in librarian.readlines():
        returnList.append(line.split("¬"))

    return returnList


def orderMtgCsv(cardCSV, setCSV):
    orderedMtgArray = []

    # loops through all cards and searches for cards
    for set in setCSV:
        for num in range(int(set[3]) + 1):
            for card in cardCSV:
                if card[0] == ("M" + set[1].lower() + str(num)):
                    orderedMtgArray.append(card)
                    break
    
    return orderedMtgArray


orderSetCSVByDate.sortSets()

app = Flask(__name__)

cards = importCSV()
sets = importSetCSV()
cardsLength = len(cards)
orderedMtg = orderMtgCsv(cards, sets)
orderedMtgLength = len(orderedMtg)



@app.route('/')
def index():
    return render_template("index.html", cards=cards)

@app.route('/about/')
def about():
    return render_template("about.html", cards=cards)

@app.route('/contact-me/')
def contact():
    return render_template("contact.html", cards=cards)

@app.route('/magic-card-database/page<num>/')
def mtgDatabase(num):
    return render_template("mtg-database.html", cards=orderedMtg, pageNum=num, length=orderedMtgLength)

@app.route('/tcg-master-base_M<magic_set_img>-set.png/')
def MTGSetImage(magic_set_img):
    print(sets)
    for set in sets:
        if set[1] == magic_set_img:
            url_for('static', filename=sets[set[0] - 1][4])

@app.route('/magic-card-database/<magic_card_id>/')
def singleCards(magic_card_id):
    for card in cards:
        if card[0] == magic_card_id and card[1] == "MTG":
            return render_template("magic-card.html", value=card, setCSV=sets, cards=cards)
    

if __name__ == "__main__":
    sqlCreateDb.createTable
    app.run(debug=True)