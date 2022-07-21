from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
from main import *
from main import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from d2_add_cargo import dd_plot
import Classes
from PyQt5.QtGui import QPainter, QColor, QPen,QTransform
import numpy
import cv2

# Наследуемся от QMainWindow
class MainWindow(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 400))  # Устанавливаем размеры
        self.setWindowTitle("Таблица гидростатики")  # Устанавливаем заголовок окна
        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет

        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в центральный виджет

        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(2)  # Устанавливаем две колонки
        table.setRowCount(6)  # и шесть строк в таблице

        # Устанавливаем заголовки таблицы
        table.setHorizontalHeaderLabels(["Водоизмещение Т.", "Осадка М."])

        # Устанавливаем всплывающие подсказки на заголовки
        table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        table.horizontalHeaderItem(1).setToolTip("Column 2 ")

        # Устанавливаем выравнивание на заголовки
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)

        TableDisplacement = gidro_table()
        print(TableDisplacement)
        # заполняем первую строку
        i = 0
        for line in TableDisplacement:
            text1 = QTableWidgetItem(str(line[0])[0:7])
            text1.setFlags(Qt.ItemIsEnabled)
            table.setItem(i, 0, text1)
            text2 = QTableWidgetItem(str(line[1])[0:7])
            text2.setFlags(Qt.ItemIsEnabled)
            table.setItem(i, 1, text2)
            i += 1

        # делаем ресайз колонок по содержимому
        table.resizeColumnsToContents()

        grid_layout.addWidget(table, 0, 0)  # Добавляем таблицу в сетку


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    parse(r'C:\Users\1\Desktop\диплом\Делюков Отчёт по ВКР.docx')

    # mw = MainWindow()
    # mw.show()
    sys.exit(app.exec())