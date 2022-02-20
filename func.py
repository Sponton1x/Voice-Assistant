import random
import sqlite3

def randoming(board):
    random.choice(board)

def createTable(nameDB, nametable, column1, Type, column2, ):
    con = sqlite3.connect(nameDB)
    cur = con.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {nametable} ({column1} {Type}, {column2} {Type});")
    con.commit()
    con.close()

def insert(nameDB, args1, args2 ):
    con = sqlite3.connect(nameDB)
    cur = con.cursor()
    cur.execute(f"INSERT INTO urls VALUES ('{args1}','{args2})")
    con.commit()
    con.close()