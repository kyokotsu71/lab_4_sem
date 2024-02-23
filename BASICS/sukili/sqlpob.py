import sqlite3

x = int(input('Введите год выпуска фильмов: '))

connection = sqlite3.connect('../../../../OneDrive/Рабочий стол/SQLiteStudio/123/films_db.sqlite')
curs = connection.cursor()

query_string = f'SELECT * FROM films WHERE year = {x};'
result = curs.execute(query_string)

for row in result:
    print(row)
connection.close()
