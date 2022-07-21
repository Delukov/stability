import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen,QTransform
from PyQt5.QtCore import Qt
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets

# from main import *
# from d2_add_cargo import dd_plot
import numpy
# import Classes


x = []
y = []
class Example(QWidget):

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
        global x, y
        q = []
        w = []
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        for i in range(len(x)):
            # q.append((x[i]*12)+500)
            # w.append((y[i]*12)+100)
            q.append(x[i]*10-380)
            w.append(y[i]*10-100)
        for i in range(len(x)-1):
                qp.drawLine(q[i], w[i], q[i+1], w[i+1])

    def event(self, e):
        "Считываем нажатие кнопки мыши в окне, координаты заносим в класс, дополняющий класс модели судна"
        cntr = []
        if e.type() == QtCore.QEvent.MouseButtonPress:
            print("Совершен клик мышью. Координаты:", e.x(), e.y())
            x1 = ((e.x()) / 10)*(-1) + 38
            y1 = ((100 - e.y())) /10
            some_ship_info.grav_centr[0] = ((e.x() - 4) / 10)*(-1) + 36
            some_ship_info.grav_centr[1] = ((105 - e.y()- 5) ) /10
            for i in range(len(x)):
                cntr.append((x[i], y[i]))
            ctr = numpy.array(cntr, dtype=int)
            print(some_ship_info.grav_centr)
            dist = cv2.pointPolygonTest(ctr, (int(x1), int(y1)), False)
            if dist == 1:
                "вызвать некст окно"

                self.close()
            else:
                self.error_dialog = QtWidgets.QErrorMessage()
                self.error_dialog.showMessage('Проверьте корректность данных и выберите точку ещё раз')
            print(dist)

        # Событие отправляется дальше

        return QWidget.event(self, e)

class file_er(QtWidgets.QErrorMessage):
     def __init__(self):
          super().__init__()

          self.initUI()

     def initUI(self):
        self.error_dialog = QtWidgets.QErrorMessage()
        self.error_dialog.showMessage('Проверьте правильность введённых данных, и попробуйте снова!')
        self.close()

if __name__ == '__main__':
    # parse('read.txt')
    # x, y = dd_plot()
    app = QApplication(sys.argv)
    ex = file_er()
    sys.exit(app.exec_())