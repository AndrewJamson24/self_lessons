import sqlite3
import sqlite3 as sq
from datetime import datetime

def create_table_db():
    """
    Функция для создания базы данных
    """
    try:
        with sq.connect('search_history_db') as con:
            db = con.cursor()
            db.execute("""
                CREATE TABLE IF NOT EXISTS search_history (
                user_name TEXT NOT NULL,
                searched_product TEXT NOT NULL,
                searched_quntity TEXT NOT NULL,
                searched_kcal_min TEXT NOT NULL,
                searched_kcal_max TEXT ,
                time TEXT NOT NULL
                )""")
    except sqlite3.Error:
        return False

def insert_entry(user_data, search_data):
    """
    Фкнуция для вписания в базы данных
    :param user_data: имя пользователя
    :param search_data: поиска которой прошел все проверки
    """
    try:
        with sq.connect('search_history_db') as con:
            db = con.cursor()
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S ")
            if len(search_data) == 3:
                db.execute("INSERT INTO search_history(user_name,searched_product,searched_quntity,searched_kcal_min,searched_kcal_max,time) "
                           "VALUES (?,?,?,?,?,?)", (user_data, search_data[0], search_data[1], search_data[2],0,dt_string))
            else:
                db.execute("INSERT INTO "
                           "search_history(user_name,searched_product,searched_quntity,searched_kcal_min, searched_kcal_max,"
                           "time) "
                           "VALUES (?,?,?,?,?,?)", (user_data, search_data[0], search_data[1], search_data[2], search_data[3],
                                                 dt_string))
    except sqlite3.Error:
        return False


def get_history(name):
    try:
        with sq.connect('search_history_db') as con:
            db = con.cursor()
            db.execute("""
                    SELECT *
                    FROM search_history
                    WHERE user_name=?
                    ORDER BY time ASC
                    LIMIT 10
                    """,(name,))
            records =db.fetchall()
            return records
    except sqlite3.Error:
        return False
