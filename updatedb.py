import sqlite3

db = sqlite3.connect('mydatabase.db')

cursor = db.cursor()

#cursor.execute('''DROP TABLE people''')
cursor.execute('''CREATE TABLE IF NOT EXISTS people (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    desc TEXT)''')

cursor.execute('''INSERT INTO people (name, desc) VALUES (?, ?)''', ('John', 'likes planes'))
cursor.execute('''INSERT INTO people (name, desc) VALUES (?, ?)''', ('Jane', 'likes planes'))

db.commit()

cursor.execute('''SELECT * FROM people''')

str_db_stuff = "Please take this data, and return names of people with similar\
    backgrounds or interests in their description fields (the field just following\
    the name). Please only return if you would rate the similarity score above 70%: \n"
for row in cursor.fetchall():
    str_db_stuff = str_db_stuff + "\n" + "Name: " + row[1] + "Description: " + row[2]
    print(row)

db.close()
