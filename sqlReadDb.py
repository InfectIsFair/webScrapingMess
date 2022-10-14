import sqlite3
from sqlite3 import Error

def connectToDb(dbDirectory):
    conn = None

    try:
        conn = sqlite3.connect(dbDirectory)
    except Error as e:
        print(e)
    
    return conn


def selectAllItems(conn, table):
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table + "Table")
    tableItems = cur.fetchall()

    for item in tableItems:
        print(item)


def main():
    database = "cards.db"

    conn = connectToDb(database)
    with conn:
        print("Card table:")
        selectAllItems(conn, "card")
        print("\nSet table:")
        selectAllItems(conn, "set")
        print("\nRarity table:")
        selectAllItems(conn, "rarity")
        print("\nText table:")
        selectAllItems(conn, "text")
        print("\nTCG table:")
        selectAllItems(conn, "tcg")


if __name__ == "__main__":
    main()