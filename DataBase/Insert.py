import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('GameOfThrones.db')
        return con
    except Error:
        print(Error)


def sql_input(con, table,data):
    try:
        cursorObj = con.cursor()
        ID_current = cursorObj.execute('Select max(id) from '+table).fetchone()[0]
        print(ID_current)
        if ID_current == None:
            ID_current = 0
        else:
            ID_current += 1
        cursorObj.execute('Insert into ' + table + ' values(' + str(ID_current) + ',' + data + ')')
        con.commit()
        print('sucsses Insert ')
    except Error as err:
        print(err)


def sql_input_non_id(con, table,data):
    try:
        cursorObj = con.cursor()
        cursorObj.execute('Insert into ' + table + ' values(' + data + ')')
        con.commit()
        print('sucsses Insert ')
    except Error as err:
        print(err)
"""
def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

"""
con = sql_connection()
con.cursor().execute('')
con.commit()

# empPhoto = convertToBinaryData('ДжонСноу.jpg')
# print(empPhoto)
"""
sql_input(con, 'Character', "'Джон', 'Сноу', -1, 1, 2, 3, 22, 'ДжонСноу.jpg', 'Вечно ничего не знает', 'Дейнерис'")
sql_input(con, 'Character', "'Дейнерис', 'Таргариен', 806020, 1, 54, 55, 22, 'ДейнерисТаргариен.jpg', 'Мать драконов', 'Дейнерис'")
sql_input(con, 'Character', "'Рейгар', 'Таргариен', 0, 3, 54, 55, 23, 'РейгарТаргариен.jpg', 'Носил красные доспехи', 'Рейгар'")
sql_input(con, 'Character', "'Лиана', 'Старк', 0, 2, 56, 57, 17, 'ЛианаСтарк.jpg', 'Леди Винтерфелла', 'Рейгар'")
sql_input(con, 'Character', "'Арья', 'Старк', -1, -1, 60, 61, 17, 'АрьяСтарк.jpg', 'Valar Morgulis', 'Бран Старк'")
"""
print(con.cursor().execute('select * from Character').fetchall())
"""
sql_input(con, 'Actor', "'Кит', 'Харингтон', 'ДжонСноу.jpg', 33, 'UK', 'Женат на Роуз Лессли' ")
sql_input(con, 'Actor', "'Эмилия', 'Кларк', 'ДейнерисТаргариен.jpg', 33, 'UK', 'Снималась в терминаторе' ")
sql_input(con, 'Actor', "'Уилф', 'Сколдинг', 'РейгарТаргариен.jpg', 30, 'UK', 'Малоизвесный актёр' ")
sql_input(con, 'Actor', "'Эшлинг', 'Франчози', 'ЛианаСтарк.jpg', 27, 'UK', 'Ирландская актриса' ")
sql_input(con, 'Actor', "'Мэйси', 'Уильямс', 'АрьяСтарк.jpg', 23, 'UK', 'Две номинации на премию Эмми' ")
"""
print(con.cursor().execute('select * from Actor').fetchall())
"""
sql_input(con, 'House', "'Старк', 'Север', 'Зима близко', 'Дом Старк' ")
sql_input(con, 'House', "'Ланнистеры', 'Запад', 'Услышь мой рёв', 'Дом ланнистеров' ")
sql_input(con, 'House', "'Грейджои', 'Железные  острова', 'Мы не сеем', 'Дом' ")
sql_input(con, 'House', "'Мартеллы', 'Дорн', 'Непреклонные, несгибаемые, несдающиеся', 'Ещё один дом' ")
"""
print(con.cursor().execute('select * from House').fetchall())
"""
sql_input(con, 'Castle', "'Винтерфелл', 'Самый лучший замок Севера' ")
sql_input(con, 'Castle', "'Красный замок', 'Укрепление в Королевской гавани' ")
sql_input(con, 'Castle', "'Хайгарден', 'Родовой замок Тиреллов' ")
sql_input(con, 'Castle', "'Пайк', 'Чертог на Железных островах' ")
sql_input(con, 'Castle', "'Штормовой предел', 'Непреступная крепость' ")
"""
print(con.cursor().execute('select * from Castle').fetchall())
"""
sql_input_non_id(con, 'Character_Actor', " 0, 0, 0")
sql_input_non_id(con, 'Character_Actor', " 1, 1, 0")
sql_input_non_id(con, 'Character_Actor', " 2, 2, 0")
sql_input_non_id(con, 'Character_Actor', " 3, 3, 0")
sql_input_non_id(con, 'Character_Actor', " 4, 4, 0")
"""
print(con.cursor().execute('select * from Character_Actor').fetchall())

"""
sql_input(con, 'User', "'admin','admin','1'")
"""
print(con.cursor().execute('select * from User').fetchall())