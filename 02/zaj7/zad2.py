import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS
               ksiazki(tytul text, autor text, rokwyd integer)
               ''')
cursor.execute('''INSERT INTO ksiazki VALUES('rzeznia nr 5', 'Kurt Vonnegut', 1956)''')
connection.commit()
cursor.execute('''INSERT INTO ksiazki VALUES('Ania z zielonego wzgórza', 'Lucy Maud Montgomery', 1990)''')
connection.commit()

cursor.execute('DELETE FROM ksiazki').rowcount, "rows"
print("po usunieciu: " )
for i in cursor.execute('SELECT * FROM ksiazki'):
    print(i)
connection.rollback()
print("po cofnieciu: " )
for i in cursor.execute('SELECT * FROM ksiazki'):
    print(i)
    

    
connection.close()
