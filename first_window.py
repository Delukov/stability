# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
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

# class error():
#
#
# def file_bag():
#     err = error()


class TableWindow(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 400))  # Устанавливаем размеры
        self.setWindowTitle("Таблица гидростатики")  # Устанавливаем заголовок окна
        self.setGeometry(1400,100,300,400)
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
    def cls(self):
        self.close()


class get_weight_window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setObjectName("Dialog")
        self.resize(212, 105)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(110, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label.setObjectName("label")
        self.pushButton.clicked.connect(self.set_weight)
        self.show()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog1", "Vol"))
        self.pushButton.setText(_translate("Dialog1", "Ок"))
        self.label.setText(_translate("Dialog1", "Введите вес судна"))

    def set_weight(self):
        # global some_ship_info
        try:
            some_ship_info.weight = float(self.lineEdit.text())
            if ((some_ship_info.weight < ((calculate_vol() * 1030)/5000)) and (some_ship_info.weight > ((calculate_vol() * 1030)/10000))):
                self.close()
                self.dd = dd_projection()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Информация")
                msg.setText("Проверьте правильность введённых данных, и попробуйте снова!")
                okButton = msg.addButton('Окей', QtWidgets.QMessageBox.AcceptRole)
                msg.addButton('Отмена', QtWidgets.QMessageBox.RejectRole)
                msg.exec()
        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Информация")
            msg.setText("Введён неверный формат строки.")
            okButton = msg.addButton('Окей', QtWidgets.QMessageBox.AcceptRole)
            msg.addButton('Отмена', QtWidgets.QMessageBox.RejectRole)
            msg.exec()
            return


class dd_projection(QtWidgets.QWidget):

         def __init__(self):
             super().__init__()

             self.initUI()

         def initUI(self):
             self.setGeometry(300, 300, 780, 105)
             self.setWindowTitle('Нажмите левой кнопкой на модели, где расположен ЦТ судна')
             self.show()

         def paintEvent(self, e):

             qp = QPainter()
             qp.begin(self)
             qp.rotate(180)
             self.drawLines(qp)
             qp.end()

         def drawLines(self, qp):
             x,y = get_proj()
             q = []
             w = []
             pen = QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
             qp.setPen(pen)
             for i in range(len(x)):
                 q.append(x[i] * 10 - 380)
                 w.append(y[i] * 10 - 100)
             for i in range(len(x) - 1):
                 qp.drawLine(q[i], w[i], q[i + 1], w[i + 1])

         def game_over(self):
             window1 = self.sh1
             window1.close()
             # show_ship_front.cls()
             # TableWindow.cls()
             self.close()

         def event(self, e):
             "Считываем нажатие кнопки мыши в окне, координаты заносим в класс, дополняющий класс модели судна"
             x,y = get_proj()
             cntr = []
             if e.type() == QtCore.QEvent.MouseButtonPress:
                 print("Совершен клик мышью. Координаты:", e.x(), e.y())
                 x1 = ((e.x()) / 10) - 38
                 y1 = ((100 - e.y())) / 10
                 some_ship_info.grav_centr[0] = ((e.x() - 4) / 10) - 36
                 some_ship_info.grav_centr[1] = ((105 - e.y() - 5)) / 10
                 for i in range(len(x)):
                     cntr.append((x[i], y[i]))
                 ctr = numpy.array(cntr, dtype=int)
                 print(some_ship_info.grav_centr)
                 dist = cv2.pointPolygonTest(ctr, (int(x1), int(y1)), False)
                 if dist == 1:
                     "вызвать некст окно"
                     # self.sh1 = show_ship_front()
                     self.sh2 = show_ship()
                     # self.Table = TableWindow()
                     # self.Table.show()

                     self.close()
                 else:
                     self.error_dialog = QtWidgets.QErrorMessage()
                     self.error_dialog.showMessage('Проверьте корректность данных и выберите точку ещё раз')
                 print(dist)

             # Событие отправляется дальше

             return QWidget.event(self, e)


class get_vol_window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setObjectName("Dialog")
        self.resize(212, 105)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(110, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label.setObjectName("label")
        self.pushButton.clicked.connect(self.valid)
        self.show()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog1", "Vol"))
        self.pushButton.setText(_translate("Dialog1", "Ок"))
        self.label.setText(_translate("Dialog1", "Введите объём судна"))

    def valid(self):
        try:
            val = validation(float(self.lineEdit.text()))
        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Информация")
            msg.setText("Введён неверный формат строки.")
            okButton = msg.addButton('Окей', QtWidgets.QMessageBox.AcceptRole)
            msg.addButton('Отмена', QtWidgets.QMessageBox.RejectRole)
            msg.exec()
            return
        if val:
            self.Wei_win = get_weight_window()
            self.close()
        else:
            self.main_win = Main_window()
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.showMessage('Проверьте правильность введённых данных, и попробуйте снова!')
            self.close()


class Main_window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.IsParse = False
        self.initUI()

    def initUI(self):
        self.setObjectName("Dialog")
        self.resize(400, 299)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(90, 10, 211, 51))
        font = QtGui.QFont()
        font.setFamily("18thCentury")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 210, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.vol)
        self.toolButton = QtWidgets.QToolButton(self)
        self.toolButton.setGeometry(QtCore.QRect(160, 110, 51, 41))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.get_f)
        self.show()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Укажите путь к файлу"))
        self.pushButton_2.setText(_translate("Dialog", "Продолжить"))
        self.toolButton.setText(_translate("Dialog", "..."))

    def vol(self):
        if IsP() == True:
            self.vol_win = get_vol_window()
            self.close()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Информация")
            msg.setText("Для начала - выберите файл")
            okButton = msg.addButton('Окей', QtWidgets.QMessageBox.AcceptRole)
            msg.addButton('Отмена', QtWidgets.QMessageBox.RejectRole)
            msg.exec()
    def get_f(self):
        get_file()
        # self.IsParse = True


class show_ship_front(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 100
        self.top = 100
        self.title = 'Вид на судно в нос'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PltCanvas(self, width=5, height=4)
        m.move(0, 0)

        # button = QPushButton('Close', self)
        # button.setToolTip('Закрыть форму')
        # button.move(500, 0)
        # button.resize(140, 100)
        # button.clicked.connect(self.cls)
        self.show()

    def cls(self):
        self.close()


class PltCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=1, height=3, dpi=100):
        # fig = Figure(figsize=(width, height), dpi=dpi)
        # self.axes = fig.add_subplot()
        self.axes = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvasQTAgg.__init__(self, Figure(figsize=(width, height), dpi=dpi))
        self.setParent(parent)

        # FigureCanvasQTAgg.setSizePolicy(self,
        #         QSizePolicy.Expanding,
        #         QSizePolicy.Expanding)
        # FigureCanvasQTAgg.updateGeometry(self)
        self.plot()

    def plot(self):
        ax = self.figure.add_subplot()
        b = []
        c = []
        for lin in Part2:
            ax.plot(lin.x, lin.y, '-', color='blue', linewidth=0.5)
            a = lin.x
            for i in a:
                i *= (-1)
                b.append(i)
            for i in lin.y:
                c.append(i)
            ax.plot(b, c, '-', color='blue', linewidth=0.5)
            b = []
            c = []
        ax.set_title('Вид на слои в нос')
        self.draw()


class show_ship(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 750
        self.top = 100
        self.title = 'Вид на судно сбоку'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=5, height=4)
        m.move(0, 0)

        button = QPushButton('Продолжить', self)
        button.setToolTip('Закрыть форму')
        button.move(500, 0)
        button.resize(140, 100)
        button.clicked.connect(self.cls)
        self.ShowFront = show_ship_front()
        self.Table = TableWindow()
        self.Table.show()
        self.show()

    def cls(self):
        self.add_cargo = dd_add_cargo()
        self.ShowFront.close()
        self.Table.close()
        self.close()


class PlotCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=1, height=3, dpi=100):
        # fig = Figure(figsize=(width, height), dpi=dpi)
        # self.axes = fig.add_subplot()
        self.axes = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvasQTAgg.__init__(self, Figure(figsize=(width, height), dpi=dpi))
        self.setParent(parent)

        # FigureCanvasQTAgg.setSizePolicy(self,
        #         QSizePolicy.Expanding,
        #         QSizePolicy.Expanding)
        # FigureCanvasQTAgg.updateGeometry(self)
        self.plot()

    def plot(self):
        z, y = dd_plot()
        ax = self.figure.add_subplot()
        ax.plot(z, y)
        ax.set_title('Судно сбоку')
        self.draw()

    def event(self, e):
        # if e.type() == QtCore.QEvent.KeyPress:
        #     print("Вы нажали клавишу на клавиатуре")
        #     print("Код:", e.key(), ", текст:", e.text())
        # elif e.type() == QtCore.QEvent.Close:
        #     print("Вы закрыли окно")
        if e.type() == QtCore.QEvent.MouseButtonPress:
            print("Совершен клик мышью. Координаты:", e.x(), e.y())
        # Событие отправляется дальше
        return QWidget.event(self, e)


class dd_add_cargo(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 780, 105)
        self.setWindowTitle('Нажмите левой кнопкой на модели, где расположен центр масс груза')
        # dd_projection.sh1.cls()
        # dd_projection.Table.cls()
        self.show()

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        qp.rotate(180)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        x, y = get_proj()
        q = []
        w = []
        pen = QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        for i in range(len(x)):
            q.append(x[i] * 10 - 380)
            w.append(y[i] * 10 - 100)
        for i in range(len(x) - 1):
            qp.drawLine(q[i], w[i], q[i + 1], w[i + 1])

    def event(self, e):
        "Считываем нажатие кнопки мыши в окне, координаты заносим в класс, дополняющий класс модели судна"
        x, y = get_proj()
        cntr = []
        if e.type() == QtCore.QEvent.MouseButtonPress:
            print("Совершен клик мышью. Координаты:", e.x(), e.y())
            x1 = ((e.x()) / 10) - 38
            y1 = ((100 - e.y())) / 10
            cargo_info.mass_center[0] = ((e.x() - 4) / 10) - 36
            cargo_info.mass_center[1] = ((105 - e.y() - 5)) / 10
            print(cargo_info.mass_center)
            for i in range(len(x)):
                cntr.append((x[i], y[i]))
            ctr = numpy.array(cntr, dtype=int)
            dist = cv2.pointPolygonTest(ctr, (int(x1), int(y1)), False)
            if (dist == 1) or (dist == 0):
                "вызвать некст окно"
                self.sh1 = get_cargo_weight()
                self.close()
            else:
                self.error_dialog = QtWidgets.QErrorMessage()
                self.error_dialog.showMessage('Проверьте корректность данных и выберите точку ещё раз')
            print(dist)

        # Событие отправляется дальше

        return QWidget.event(self, e)


class get_cargo_weight(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setObjectName("Dialog")
        self.resize(212, 105)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(110, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 180, 16))
        self.label.setObjectName("label")
        self.pushButton.clicked.connect(self.set_weight)
        self.show()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog1", "Vol"))
        self.pushButton.setText(_translate("Dialog1", "Ок"))
        self.label.setText(_translate("Dialog1", "Введите вес груза в тоннах"))

    def set_weight(self):
        # global some_ship_info
        try:
            cargo_info.weight = float(self.lineEdit.text())
        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Информация")
            msg.setText("Введён неверный формат строки.")
            okButton = msg.addButton('Окей', QtWidgets.QMessageBox.AcceptRole)
            msg.addButton('Отмена', QtWidgets.QMessageBox.RejectRole)
            msg.exec()
            return
        if (some_ship_info.weight / 5 >= cargo_info.weight):
            recalc()
            self.Last = last_proj()
            self.close()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Информация")
            msg.setText("Некорректный вес груза.")
            okButton = msg.addButton('Окей', QtWidgets.QMessageBox.AcceptRole)
            msg.addButton('Отмена', QtWidgets.QMessageBox.RejectRole)
            msg.exec()


class LastPlot(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=1, height=3, dpi=100):
        # fig = Figure(figsize=(width, height), dpi=dpi)
        # self.axes = fig.add_subplot()
        self.axes = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvasQTAgg.__init__(self, Figure(figsize=(width, height), dpi=dpi))
        self.setParent(parent)

        # FigureCanvasQTAgg.setSizePolicy(self,
        #         QSizePolicy.Expanding,
        #         QSizePolicy.Expanding)
        # FigureCanvasQTAgg.updateGeometry(self)
        self.plot()

    def plot(self):
        z, y = dd_plot()
        ax = self.figure.add_subplot()
        ax.plot(z, y)
        ax.scatter(some_ship_info.grav_centr[0], some_ship_info.grav_centr[1])
        ax.scatter(cargo_info.mass_center[0], cargo_info.mass_center[1])
        ax.set_title('Судно сбоку')
        self.draw()


class last_proj(QMainWindow):
    """ метацентр
    """
    def __init__(self):
        super().__init__()
        self.left = 750
        self.top = 100
        self.title = 'Вид на судно сбоку'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = LastPlot(self, width=5, height=4)
        m.move(0, 0)
        button = QPushButton('Продолжить', self)
        button.setToolTip('Закрыть форму')
        button.move(500, 0)
        button.resize(140, 100)
        button.clicked.connect(self.cls)
        self.DraftLabel = QtWidgets.QLabel(self)
        # DraftLabel.resize(100,100)
        # DraftLabel.move(500,200)
        self.DraftLabel.setGeometry(QtCore.QRect(500,200,500,100))
        self.Draft = 'Осадка:' + str(GetDraft())[0:7]
        self.DraftLabel.setText(self.Draft)

        self.show()

    def cls(self):

        self.close()

# class Table_with_draft():

# class file_er(QtWidgets.QErrorMessage):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#     def initUI(self):
#         self.error_dialog = QtWidgets.QErrorMessage()
#         self.error_dialog.showMessage('Проверьте правильность введённых данных, и попробуйте снова!')
#         self.close()



