import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('GameOfThrones.db')
        return con
    except Error:
        print(Error)


def sql_init(con, table):
    cursorObj = con.cursor()
    cursorObj.execute('create table if not exists ' + table)
    con.commit()


def sql_drop(con, table):
    cursorObj = con.cursor()
    cursorObj.execute('drop table if exists ' + table)
    con.commit()


con = sql_connection()
con.cursor().execute('PRAGMA foreign_keys = ON')
con.commit()
# con.cursor().execute('drop table if exists Character')
# con.commit()
# con.cursor().execute('drop table if exists Actor')
# con.commit()
"""
sql_drop(con, 'Character_Actor')
sql_drop(con, 'Character_House')
sql_drop(con, 'House_Castle')
sql_drop(con, 'Vassal')
sql_drop(con, 'House_Head')
sql_drop(con, 'Character')
sql_drop(con, 'Actor')
sql_drop(con, 'House')
sql_drop(con, 'Castle')
sql_drop(con, 'User')
"""


sql_init(con, 'Character(id integer PRIMARY KEY, '
              'name text, '
              'surname text, '
              'dead integer, '
              'id_partner integer, '
              'id_mother integer, '
              'id_father integer, '
              'age integer, '
              'description text, '
              'side text)')

sql_init(con, 'Actor(id integer PRIMARY KEY, '
              'name text, '
              'surname text, '
              'age integer, '
              'country text, '
              'description text)')

sql_init(con, 'House(id integer PRIMARY KEY, '
              'name text, '
              'area text, '
              'motto text, '
              'description text)')

sql_init(con, 'Castle(id integer PRIMARY KEY, '
              'name text, '
              'description text)')

sql_init(con, 'Character_Actor(id_character integer, '
              'id_actor integer, '
              'time integer, '
              'FOREIGN KEY(id_character) REFERENCES Character(id), '
              'FOREIGN KEY(id_actor) REFERENCES Actor(id))')

sql_init(con, 'Character_House(id_character integer, '
              'id_house integer, '
              'time integer, '
              'FOREIGN KEY(id_character) REFERENCES Character(id), '
              'FOREIGN KEY(id_house) REFERENCES House(id) )')

sql_init(con, 'House_Castle(id_house integer, '
              'id_castle integer, '
              'time integer, '
              'FOREIGN KEY(id_house) REFERENCES House(id), '
              'FOREIGN KEY(id_castle) REFERENCES Castle(id) )')

sql_init(con, 'Vassal(id_owner integer, '
              'id_vassal integer, '
              'time integer, '
              'FOREIGN KEY(id_owner) REFERENCES House(id), '
              'FOREIGN KEY(id_vassal) REFERENCES House(id))')

sql_init(con, 'House_Head(id_character integer, '
              'id_house integer, '
              'time integer, '
              'FOREIGN KEY(id_character) REFERENCES Character(id), '
              'FOREIGN KEY(id_house) REFERENCES House(id) )')

sql_init(con, 'User(id integer PRIMARY KEY, '
              'login text, '
              'password text, '
              'admin tinyint(1) DEFAULT 0)')
