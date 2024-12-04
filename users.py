import sqlite3

def adding(log,psw):
    """
    Добавление нового пользователя в БД
    Принимает на вход уникальный логин и хэш соответствующего пароля
    Вносит данные в БД
    """
    with sqlite3.connect('Users.db') as db:
        cur=db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Users(
                Login TEXT,
                Password TEXT
        )""")
        cur.execute("""
        INSERT INTO Users (Login, Password) VALUES (?,?)""", (log, psw)
        )

def checking_login(log):
    """
    Проверка наличия логина в БД
    На вход получает логин log(str) из ввода
    Возвращает True/Fasle при проверках уникальности логина и при аунтефикации
    """
    with sqlite3.connect('Users.db') as db:
        cur=db.cursor()
        cur.execute("""SELECT Login FROM Users WHERE Login=?""", (log,)
        )
        res_def=cur.fetchone()
        if res_def:
            return True
        return False

def hashed_password(log):
    """
    Получение хэша пароля из БД
    На вход получает логин log(str) при авторизации
    Возвращает хэш пароля для соответствующего логина
    """
    with sqlite3.connect('Users.db') as db:
        cur=db.cursor()
        cur.execute("""
        SELECT Password FROM Users WHERE Login=?""", (log,)
        )
        res_def=cur.fetchone()
        if res_def:
            return res_def[0]
        return None