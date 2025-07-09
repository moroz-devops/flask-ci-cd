import sqlite3

def init_db():
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS users 
    ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
