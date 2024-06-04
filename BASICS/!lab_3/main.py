from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QDialog, QTableWidget, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import Qt
import sqlite3


class FilmsTable(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("mainwindow.ui", self)

        self.setWindowTitle("ФИЛЬМЫ")
        self.selected_row = None

        self.filmsTable.setColumnCount(5)
        self.filmsTable.setHorizontalHeaderLabels(["id", "Название", "Год выпуска", "Жанр", "Длительность"])
        self.filmsTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.filmsTable.doubleClicked.connect(self.edit)

        self.filmsTable.selectionModel().selectionChanged.connect(self.select_row)

        self.addButton.clicked.connect(self.add)
        self.deleteButton.clicked.connect(self.delete)

        self.load_films()

    def load_films(self):
        db_connection = sqlite3.connect("films_db.sqlite")
        cursor = db_connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS films \
                        (id INTEGER, title TEXT, year INTEGER, genre TEXT, duration INTEGER)")

        res = cursor.execute("SELECT films.id, films.title, films.year, genres.title, films.duration FROM films JOIN genres ON films.genre = genres.id")
        films = res.fetchall()

        self.filmsTable.setRowCount(len(films))
        self.filmsTable.clearContents()

        for row, film in enumerate(films):
            for column, data in enumerate(film):
                item = QTableWidgetItem(str(data))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.filmsTable.setItem(row, column, item)

        self.filmsTable.resizeColumnsToContents()
        db_connection.close()

    def select_row(self, selected):
        indexes = selected.indexes()
        if indexes:
            selected_row = indexes[0].row()

            with sqlite3.connect("films_db.sqlite") as connection:
                curs = connection.cursor()
                curs.execute("SELECT id FROM films")
                rows = curs.fetchall()

            if rows:
                film_id = rows[selected_row][0]
                self.selected_row = film_id
            else:
                self.selected_row = None

    def edit(self, index):
        row = index.row()
        film_data = []

        for column in range(self.filmsTable.columnCount()):
            item = self.filmsTable.item(row, column)
            film_data.append(item.text())

        film_id = self.filmsTable.item(row, 0).text()
        editor = FilmsEditor(film_data, int(film_id))
        if editor.exec_() == QDialog.Accepted:
            self.load_films()

    def add(self):
        editor = FilmsEditor()
        if editor.exec() == QDialog.Accepted:
            title = editor.titleEdit.text()
            year = int(editor.yearEdit.text())
            genre = editor.genreEdit.text()
            duration = int(editor.durationEdit.text())

            connection = sqlite3.connect("films_db.sqlite")
            curs = connection.cursor()

            query_string = "INSERT INTO films (title, year, genre, duration) VALUES (?, ?, ?, ?)"
            curs.execute(query_string, (title, year, genre, duration))

            connection.commit()
            connection.close()

            self.load_films()

    def delete(self):
        selected_rows = [index.row() for index in self.filmsTable.selectedIndexes()]

        if len(selected_rows) > 0:
            reply = QMessageBox.question(self, "Точно удалить????????",
                                         "Уверены?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                connection = sqlite3.connect("films_db.sqlite")
                curs = connection.cursor()

                film_id = self.selected_row
                query_string = f"DELETE FROM films WHERE id = {film_id}"
                curs.execute(query_string)

                connection.commit()
                connection.close()
                self.load_films()

class FilmsEditor(QDialog):
    def __init__(self, film_data=None, film_id=None):
        super().__init__()
        uic.loadUi("editfilm.ui", self)

        self.setWindowTitle("изменение фильма")

        self.film_id = film_id
        if film_data:
            self.titleEdit.setText(film_data[1])
            self.yearEdit.setText(str(film_data[2]))
            self.genreEdit.setText(film_data[3])
            self.durationEdit.setText(str(film_data[4]))

        self.saveButton.clicked.connect(self.save_changes)

    def save_changes(self):
        title = self.titleEdit.text()
        year = int(self.yearEdit.text())
        genre = self.genreEdit.text()
        duration = int(self.durationEdit.text())

        if self.film_id is not None and self.film_id != 0:
            connection = sqlite3.connect("films_db.sqlite")
            curs = connection.cursor()

            curs.execute("SELECT id FROM films")
            film_id = self.film_id
            query_string = f"UPDATE films SET title = ?, year = ?, genre = ?, duration = ? WHERE id = ?"
            curs.execute(query_string, (title, year, genre, duration, film_id))

            connection.commit()
            connection.close()
        else:
            connection = sqlite3.connect("films_db.sqlite")
            curs = connection.cursor()

            curs.execute("SELECT MAX(id) FROM films")
            max_id = curs.fetchone()[0]
            new_id = max_id + 1 if max_id is not None else 1

            query_string = "INSERT INTO films (id, title, year, genre, duration) VALUES (?, ?, ?, ?, ?)"

            curs.execute(query_string, (new_id, title, year, genre, duration))

            connection.commit()
            connection.close()

        self.accept()


app = QApplication([])
ex = FilmsTable()
ex.show()
app.exec()