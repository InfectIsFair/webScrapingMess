import sqlite3
from sqlite3 import Error

def connectToDb(dbDirectory):
    conn = None

    try:
        conn = sqlite3.connect(dbDirectory)
    except Error as e:
        print(e)
    
    return conn


def insertCardFile(conn, file):
    sql = """ INSERT INTO cardTable(cardId, tcgId, cardName, rarityId, setId, price, textTableLink)
              VALUES(?, ?, ?, ?, ?, ?, ?) """

    c = conn.cursor()
    c.execute(sql, file)
    conn.commit()

    return c.lastrowid


def insertSetFile(conn, file):
    sql = """ INSERT INTO setTable(setName, dateOfRelease, cardsInSet)
              VALUES(?, ?, ?) """

    c = conn.cursor()
    c.execute(sql, file)
    conn.commit()
    
    return c.lastrowid


def insertRarityFile(conn, file):
    sql = """ INSERT INTO rarityTable(rarity)
              VALUES(?) """

    c = conn.cursor()
    c.execute(sql, file)
    conn.commit()
    
    return c.lastrowid


def insertTextTableFile(conn, file):
    sql = """ INSERT INTO textTable(textTableLink, textValueId)
              VALUES(?, ?) """
    
    c = conn.cursor()
    c.execute(sql, file)
    conn.commit()
    
    return c.lastrowid


def insertTextValue(conn, file):
    sql = """ INSERT INTO textValues(textValueId, text, textOrFlavour)
              VALUES(?, ?, ?) """
    
    c = conn.cursor()
    c.execute(sql, file)
    conn.commit()
    
    return c.lastrowid


def insertTcgFile(conn, file):
    sql = """ INSERT INTO tcgTable(tcg)
              VALUES(?) """

    c = conn.cursor()
    c.execute(sql, file)
    conn.commit()
    
    return c.lastrowid

"""
example of how to insert per table

Use this | to find the Id value of the last inserted element, allowing you to fill in foreign keys
         V

SCOPE_IDENTITY() returns the last identity value generated for any table in the current session and the current scope. Generally what you want to use.


start of all insert functions:

database = "cards.db"
conn = connectToDb(database)
with conn:

insert card:
    tcgId = 1
    rarityId = 1
    setId = 1
    textTableLink = 1
    card = ("Mxln120", tcgId, "Sanctum Seeker", rarityId, setId, 0.66, textTableLink)
    insertCardFile(conn, card)

insert set:
    set = ("XLN", "2017-09-29", 289)
    insertSetFile(conn, set)

insert rarity:
    rarity = ("Rare")
    insertRarityFile(conn, rarity)

insert text:
    text = "Whenever this creature, die"
    flavour = "Litmus test"

    textTextValue = (text, 0)
    flavourTextValue = (flavour, 1)

    insertTextValue(conn, textTextValue)
    insertTextValue(conn, flavourTextValue)


insert tcg:
    tcg = ("MTG")
    insertTcgFile(conn, tcg)
"""