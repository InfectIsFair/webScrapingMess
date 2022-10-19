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
                           rarityId smallint NOT NULL,
                           price money NOT NULL,
                           textTableLink smallint NOT NULL,
                           flavourId int NOT NULL,
                           tcgId smallint NOT NULL,
                           FOREIGN KEY (rarityId) REFERENCES rarityTable (rarityId),
                           FOREIGN KEY (textTableLink) REFERENCES textTable (textTableLink),
                           FOREIGN KEY (tcgId) REFERENCES tcgTable (tcgId),
                           FOREIGN KEY (setId) REFERENCES setTable (setId)
                       );"""

    sqlCreateSet = """ CREATE TABLE IF NOT EXISTS setTable (
                           setId smallint PRIMARY KEY,
                           setName nchar(10) NOT NULL,
                           dateOfRelease date NOT NULL,
                           cardsInSet smallint NOT NULL
                       );"""
    
    sqlCreateRarity = """ CREATE TABLE IF NOT EXISTS rarityTable (
                              rarityId smallInt PRIMARY KEY,
                              rarity nchar(35) NOT NULL
                          );"""

    sqlCreateTextTable = """ CREATE TABLE IF NOT EXISTS textTable (
                             textTableLink smallint PRIMARY KEY,
                             textValueId int NOT NULL,
                             FOREIGN KEY (textValueId) REFERENCES textValues (textValueId)
                        );"""

    sqlCreateTextValue = """ CREATE TABLE IF NOT EXISTS textValues (
                             textValueId int PRIMARY KEY,
                             text nchar(1200) NOT NULL,
                             textOrFlavour bit NOT NULL
                        );"""

    sqlCreateTcg = """ CREATE TABLE IF NOT EXISTS tcgTable (
                           tcgId smallint PRIMARY KEY,
                           tcg nchar(8) NOT NULL
                       );"""

    print(sqlite3.version)
    sqlCreateList = [sqlCreateCard, sqlCreateSet, sqlCreateRarity, sqlCreateTextTable, sqlCreateTextValue, sqlCreateTcg]

    for table in sqlCreateList:
        createTable(database, table)
