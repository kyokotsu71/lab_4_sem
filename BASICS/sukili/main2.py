from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel

class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('editfilm.ui', self)
        self.pushButton.clicked.connect(self.press)

    def press(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('films_db.sqlite')
        db.open()

        model = QSqlQueryModel()
        query_string = """SELECT f.title as [Название], g.title as [Жанр], 
                f.year as [Год выпуска], f.duration as [Длительность] FROM films f JOIN genres g on f.genre = g.id;"""
        model.setQuery(query_string, db)
        self.tableWiew.setModel(model)
        self.tableView.setColumnHidden



app = QApplication([])
window = Form()
window.show()
app.exec()
