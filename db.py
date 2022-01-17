import sqlite3 as sql

# 
def ex_decorator(func):
    def wrapper(*arg):
        try:
            return func(*arg)
        except sql.Error as e:
            print(f"Ошибка БД: {e}")
        except Exception as e:
            print(f"Что-то пошло не так: {e}")
    return wrapper

# Создание БД
@ex_decorator
def create_db():
    with sql.connect("database/logs.db") as db:
        cursor = db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS log_table 
            (
                form TEXT, result TEXT
            )
            """
        )
        db.commit()

# запись в БД
@ex_decorator
def write_db(form, res):
    with sql.connect("database/logs.db") as db:
        cursor = db.cursor()
        cursor.execute(
            # f"INSERT INTO log_table VALUES ({form}, {res})"
            "INSERT INTO log_table VALUES (?, ?)",
            (form, res)
        )
        db.commit()

# чтение из БД
@ex_decorator
def read_db():
    with sql.connect("database/logs.db") as db:
        cursor = db.cursor()
        cursor.execute(
            f"SELECT * FROM log_table"
        )
        return cursor.fetchall()