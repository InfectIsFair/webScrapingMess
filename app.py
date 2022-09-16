from flask import Flask, render_template

def importCSV():
    count = -1
    returnList = []
    librarian = open('card-library.csv', 'r')
    for line in librarian.readlines():
        returnList.append(line.split(','))
        count += 1

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

# for card in cards:
#     if card[1] == "MTG":
#         @app.route("/mtg-cards/")
#         def mtgCard():
#             return render_template("card.html", value=card)
#     elif card[1] == "PTCG":
#         dnsExtension = '/ptcg-cards/' + card[0]
#         @app.route(dnsExtension)
#         def ptcgCard():
#             return render_template("cards.html", value=card)

if __name__ == "__main__":
    app.run(debug=True)
