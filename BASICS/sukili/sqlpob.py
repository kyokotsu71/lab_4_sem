import sqlite3

x = int(input('Введите год выпуска фильмов: '))

connection = sqlite3.connect('../../../../OneDrive/Рабочий стол/SQLiteStudio/123/films_db.sqlite')
curs = connection.cursor()

query_string = f'SELECT * FROM films WHERE year = {x};'
result = curs.execute(query_string)

#print(type(result.fetchall()))  # list
'''
row = result.fetchone()
print(row)

for row in result:
    print(row)
connection.close()

print(result.description)
connection.close()
'''
captions = [x[0] for x in result.description]
print(captions)
connection.close()
