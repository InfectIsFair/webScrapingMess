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
    sql = """ INSERT INTO cardTable(cardId, tcgId, cardName, rarityId, setId, price, textId, oracleId)
              VALUES(?, ?, ?, ?, ?, ?, ?) """

    c = conn.cursor()
    c.execute(sql, file)
    conn.commit()

    return c.lastrowid


def insertSetFile(conn, file):
    sql = """ INSERT INTO setTable(setId, setName, dateOfRelease, cardsInSet)
              VALUES(?, ?, ?, ?) """

    c = conn.cursor()
    c.execute(sql, file)
    conn.commit()
    
    return c.lastrowid


def insertRarityFile(conn, file):
    sql = """ INSERT INTO rarityTable(rarityId, rarity)
              VALUES(?, ?) """

    c = conn.cursor()
    c.execute(sql, file)
    conn.commit()
    
    return c.lastrowid


def insertTextFile(conn, file):
    sql = """ INSERT INTO textTable(textId, text, oracleOrFlavour)
              VALUES(?, ?, ?) """
    
    c = conn.cursor()
    c.execute(sql, file)
    conn.commit()
    
    return c.lastrowid


def insertFlavourFile(conn, file):
    sql = """ INSERT INTO flavourTable(textId, text)
              VALUES(?, ?) """
    
    c = conn.cursor()
    c.execute(sql, file)
    conn.commit()
    
    return c.lastrowid


def insertTcgFile(conn, file):
    sql = """ INSERT INTO tcgTable(tcgId, tcg)
              VALUES(?, ?) """

    c = conn.cursor()
    c.execute(sql, file)
    conn.commit()
    
    return c.lastrowid


# example of how to insert per table

# start of all

# database = "cards.db"
# conn = connectToDb(database)
# with conn:

# insert card
    # card = ("Mxln120", 1, "Sanctum Seeker", 1, 0.66, 1, 2)
    # insertCardFile(conn, card)

# insert set
    # set = (1, "XLN", "2017-09-29", 289)
    # insertSetFile(conn, set)

# insert rarity
    # rarity = (1, "Rare")
    # insertRarityFile(conn, rarity)

# insert text (oracle & flavour)
    # oracle = (1, "Litmus", 0)
    # flavour = (2, "Slithering Slippery Slinking Sneaky Superficial Sugestive Smart Snake", 1)
    # insertTextFile(conn, oracle)
    # insertTextFile(conn, flavour)

# insert tcg
    # tcg = (1, "MTG")
    # insertTcgFile(conn, tcg)