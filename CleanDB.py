import sqlite3

db=sqlite3.connect('Users.db')
cur=db.cursor()
cur.execute("""
DROP TABLE Users
""")
db.commit()
db.close()