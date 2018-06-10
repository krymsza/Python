import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS
               ksiazki(tytul text, autor text, rokwyd integer)
               ''')
cursor.execute('''INSERT INTO ksiazki VALUES('rzeznia nr 5', 'Kurt Vonnegut', 1956)''')
cursor.execute('''INSERT INTO ksiazki VALUES('Ania z zielonego wzgórza', 'Lucy Maud Montgomery', 1990)''')
cursor.execute('DELETE FROM ksiazki WHERE rokwyd < 1950')

for i in cursor.execute('SELECT DISTINCT * FROM ksiazki'):
    print(i)

connection.close()
