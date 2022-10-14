import sqlite3
from sqlite3 import Error

def createTable(dbDirectory, sqlStatement):
    conn = None

    try:
        conn = sqlite3.connect(dbDirectory)
    except Error as e:
        print(e)

    try:
        c = conn.cursor()
        c.execute(sqlStatement)
    except Error as e:
        print(e)
    finally:
        conn.close()


def main():
    database = "cards.db"

    sqlCreateCard = """CREATE TABLE IF NOT EXISTS cardTable (
                           cardId nchar(9) PRIMARY KEY,
                           setId smallint NOT NULL,
                           cardName nchar(80) NOT NULL,
                           rarityId smallint(3) NOT NULL,
                           price money NOT NULL,
                           textId int NOT NULL,
                           flavourId int NOT NULL,
                           tcgId smallint(10) NOT NULL,
                           FOREIGN KEY (rarityId) REFERENCES rarityTable (rarityId),
                           FOREIGN KEY (textId) REFERENCES textTable (textId),
                           FOREIGN KEY (flavourId) REFERENCES flavourTable (flavourId),
                           FOREIGN KEY (tcgId) REFERENCES tcgTable (tcgId),
                           FOREIGN KEY (setId) REFERENCES setTable (setId)
                       );"""

    sqlCreateSet = """ CREATE TABLE IF NOT EXISTS setTable (
                           setId smallint PRIMARY KEY,
                           setName nchar(10) NOT NULL,
                           dateOfRelease date NOT NULL,
                           cardsInSet smallint(4) NOT NULL
                       );"""
    
    sqlCreateRarity = """ CREATE TABLE IF NOT EXISTS rarityTable (
                              rarityId smallInt(3) PRIMARY KEY,
                              rarity nchar(35) NOT NULL
                          );"""

    sqlCreateText = """ CREATE TABLE IF NOT EXISTS textTable (
                            textId int PRIMARY KEY,
                            text nchar(1200) NOT NULL,
                        );"""

    sqlCreateFlavour = """ CREATE TABLE IF NOT EXISTS flavourTable (
                            flavourId int PRIMARY KEY,
                            flavour nchar(1200) NOT NULL,
                        );"""

    sqlCreateTcg = """ CREATE TABLE IF NOT EXISTS tcgTable (
                           tcgId smallint(10) PRIMARY KEY,
                           tcg nchar(8) NOT NULL
                       );"""

    print(sqlite3.version)
    sqlCreateList = [sqlCreateCard, sqlCreateSet, sqlCreateRarity, sqlCreateText, sqlCreateFlavour, sqlCreateTcg]

    for table in sqlCreateList:
        createTable(database, table)
