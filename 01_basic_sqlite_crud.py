import sqlite3

db = sqlite3.connect('/Users/lmuser/desktop/python_learn/python_exercise_on_sqlite_crud/01_author.sqlite')
cursor = db.cursor()
cursor.execute('''CREATE TABLE authors(id INTEGER PRIMARY KEY,
                       username TEXT unique, author_name TEXT)''')


id1 = 1
username1 = "almasud"
author_name1 = "Abdullah Al Masud"

id2 = 2
username2 = "rimon"
author_name2 = "Rimol Ali"

id3 = 3
username3 = "niloy"
author_name3 = "Niloy Roy"

id4 = 4
username4 = "sourov"
author_name4 = "Sourov Deb Sharma"

id5 = 5
username5 = "sathi"
author_name5 = "Sathi Rani Roy"

authors = [(id1, username1, author_name1),
            (id2, username2, author_name2),
            (id3, username3, author_name3),
            (id4, username4, author_name4),
            (id5, username5, author_name5)]

cursor.executemany('''INSERT INTO authors(id, username, author_name)values(?,?,?)''',authors)

db.commit()
cursor.execute('''SELECT id, author_name FROM authors''')
all_rows = cursor.fetchall()
for item in all_rows:
    print(*item, sep="-")
