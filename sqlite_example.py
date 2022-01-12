# Система управления базами данных (СУБД) SQLite3

import sqlite3 as sql
from sqlite3.dbapi2 import Error

def db_handler(path: str, command: str) -> sql.Cursor:
    try:
        # соединение с БД
        db = sql.connect(path)

        # объект курсора ("панель управления")
        cursor = db.cursor()

        # передача команд на языке SQL
        cursor.execute(command)

        # закрепление изменений
        db.commit()
    except Error as e:
        print(e)
    # finally:
    #     # закрытие базы данных
    #     db.close()

    return cursor

# относительный путь до БД
path = "database/test.db"

# создание базы данных с таблицой "test"
command = """create table test_1 
        (id integer, login text, message TEXT)"""
# _ = db_handler(path, command)

# создание таблицы с проверкой на ее существование
command = """create table if not exists test_1 
        (id integer, login text, message TEXT)"""

# создание второй таблицы с проверкой на ее существование
command = """create table if not exists test_2 
        (id integer, login text, message TEXT)"""

with sql.connect(path) as db:
    cursor = db.cursor()
    cursor.execute(command)
    cursor.execute(
        "INSERT INTO test_1 VALUES (?, ?, ?)", 
        (10, "hello", "world")
    )
    db.commit()

# запись данных в БД
# with sql.connect(path) as db:
#     cursor = db.cursor()
#     # запись данных в таблицу "test_1"
#     cursor.execute(
#         "INSERT INTO test_1 VALUES (?, ?, ?)", 
#         (10, "hello", "world")
#     )
#     db.commit()

# чтение данных из БД
command_1 = "SELECT * FROM test_1"
command_2 = "SELECT login, message FROM test_2"
try:
    # соединение с БД
    db = sql.connect(path)

    # объект курсора ("панель управления")
    cursor = db.cursor()

    # передача команд на языке SQL
    cursor.execute(command_1)
    cursor.execute(command_2)

    # закрепление изменений
    db.commit()
except Error as e:
    print(e)

# for _ in range(15):

# значение по одному
#     print(cursor.fetchone())

# определенное кол-во значений
# print(cursor.fetchmany(3))

# все значения
print(cursor.fetchall())

db.close()