from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
import sqlite3


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainwindow.ui', self)
        self.pushButton.clicked.connect(self.press)

    def press(self):

        connection = sqlite3.connect('films_db.sqlite')
        curs = connection.cursor()
        query_string = """SELECT f.title as [Название], g.title as [Жанр], 
        f.year as [Год выпуска], f.duration as [Длительность] FROM films f JOIN genres g on f.genre = g.id;"""

        result = curs.execute(query_string)
        captions = [t[0] for t in result.description]
        self.tableWidget.setColumnCount(len(captions))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(captions)

        for row in result:
            n = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(n + 1)
            k = len(row)
            for i in range(k):
                self.tableWidget.setItem(n, i,
                                         QTableWidgetItem(str(row[i])))
        self.tableWidget.resizeColumnsToContents()

        connection.close()


app = QApplication([])
window = Form()
window.show()
app.exec()
