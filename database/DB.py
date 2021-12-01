import sqlite3
from sqlite3 import Error

import Constants

# make a connection
from objects.Champion import Champion
from objects.Nickname import Nickname


def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(Constants.DB_FILE)
    except Error as e:
        print(e)

    return conn

# create one table
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)

# create one table
def alter_table(conn, alter_table_sql):
    try:
        c = conn.cursor()
        c.execute(alter_table_sql)
        conn.commit()
    except Error as e:
        print(e)

# create all tables if not exists
def create_all_tables():

    # create a database connection
    conn = create_connection()

    # create tables
    if conn is not None:
        create_table(conn, table_champions())
        create_table(conn, table_nicknames())

    else:
        print("Error! cannot create the database connection.")

# return the sql query for champions
def table_champions():
    sql_query = "CREATE TABLE IF NOT EXISTS champions (id INTEGER PRIMARY KEY, name TEXT NOT NULL);"

    return sql_query

# return the sql query for nicknames
def table_nicknames():
    sql_query = "CREATE TABLE IF NOT EXISTS nicknames (id INTEGER PRIMARY KEY, nickname TEXT NOT NULL);"

    return sql_query

# insert one register to Table Nicknames
def insert_to_nickname(nickname):
    # create a database connection
    conn = create_connection()
    with conn:
        sql = "INSERT INTO nicknames (nickname) VALUES(?)"
        cur = conn.cursor()
        task = (nickname,)
        cur.execute(sql, task)
        conn.commit()
        return cur.lastrowid

# insert all Champions
def insert_all_champions():
    # create a database connection
    conn = create_connection()
    list = ["Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion-Sol", "Azir", "Bardo", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan-IV", "Jax", "Jayce", "Jhin", "Jinx", "Kai'Sa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw", "LeBlanc", "Lee-Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master-Yi", "Miss-Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nocturne", "Nunu e Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "Rek'Sai", "Rell", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm-Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted-Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vex", "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin-Zhao", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]
    with conn:
        sql = "INSERT INTO champions (name) VALUES(?)"
        cur = conn.cursor()
        for pos in range(len(list)):
            task = (list[pos],)
            cur.execute(sql, task)
        conn.commit()
        return cur.lastrowid

# delete a register of Table Nicknames
def delete_nickname(id):
    # create a database connection
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM nicknames WHERE id = ?", (id,))
        conn.commit()
        return cur.lastrowid

# insert many registers to Table Things
def insert_to_db(conn, sql, task):
    # create a database connection
    try:
        with conn:
            cur = conn.cursor()
            cur.execute(sql, task)
            conn.commit()
            return cur.lastrowid
    except Error as e:
        print(e)

# select all champions ordering by name
def select_all_champions():
    result_list = []

    # create a database connection
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM champions ORDER BY name")

        rows = cur.fetchall()

        for row in rows:
            result_list.append(Champion(row[0], row[1], False))

    return result_list

# select all champions ordering by name
def select_all_nicknames():
    result_list = []

    # create a database connection
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT id, nickname FROM nicknames")

        rows = cur.fetchall()

        for row in rows:
            result_list.append(Nickname(row[0], row[1]))

    return result_list
