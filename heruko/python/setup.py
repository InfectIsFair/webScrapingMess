from flask import Flask, render_template
import orderSetByDate

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
        returnList.append(line.split("/"))

    return returnList


app = Flask(__name__)

cards = importCSV()
cardsLength = len(cards)

@app.route('/')
def index():
    return render_template("index.html", cards=cards)

@app.route('/about/')
def about():
    return render_template("about.html", cards=cards)

@app.route('/contact-me/')
def contact():
    return render_template("contact.html", cards=cards)

@app.route('/magic-card-database/<magic_card_id>/')
def singleCards(magic_card_id):
    for card in cards:
        if card[0] == magic_card_id:
            return render_template("magic-card.html", value=card, setCSV=importSetCSV(), cards=cards)

if __name__ == "__main__":
    app.run(debug=True)
