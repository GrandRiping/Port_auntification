import sqlite3

"""
Возможность удаления данных из БД при необходимости
"""

db=sqlite3.connect('Users.db')
cur=db.cursor()
cur.execute("""
DROP TABLE Users
""")
db.commit()
db.close()