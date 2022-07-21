from main import *
from PyQt5 import QtCore, QtGui, QtWidgets
import first_window
from PyQt5.QtWidgets import QMessageBox
Part2 = []
IsParse = False


class Part(object):
    def __init__(self, long, *points):
        self.long = long
        self.points = []
        for a in points:
            self.points.append(a)

    def add(self, point):
        self.points.append(point)


class some_ship_info:
    weight = 0
    grav_centr = [0, 0]
    meta_centr = [0, 0]
    meta_height = 0


class cargo_info:
    weight = 0
    mass_center = [0, 0]

# 1Й КЛАСС ДЛЯ РАЗБИЕНИЯ ФАЙЛА
class rab(object):

    def __init__(self, ln):
        self.ln = ln
        self.x = []
        self.y = []


    def addel(self, lin):
        for b in lin:
            a = 0
            b.strip()
            i = b
            while i[a] != ' ':
                a += 1
            if i[a - 1] == 'S':
                ch = float(i[:(a - 1)])
                ch *= (-1)
                self.x.append(ch)
            else:
                self.x.append(float(i[:(a - 1)]))
            a += 3
            if i[a] == '-':
                ch = float(i[(a + 1):])
                ch *= -1
                self.y.append(ch)
            else:
                self.y.append(float(i[a:]))

    def pri(self):
        print(self.ln, self.x, self.y)

    def modz(self):
        a = self.ln
        b = len(a)
        if a[b - 2] == "F":
            z = float(a[:(b - 2)])
        else:
            z = float(a[:(b - 2)])
            z *= -1
        return z


def parse(file):
    global Part2
    global IsParse
    Part2.clear()
    IsParse = True
    try:

        f = open(f'{file}', 'r')
        i = -1
        Part1 = []
        str = 'Long'
        for line in f:
            if line.startswith(str):
                i += 1
                Part1.append(Part(line[7:]))
            else:
                Part1[i].add(line)
        # ВЫШЕ СЧИТЫВАНИЕ
        # Part2 = []
        i = -1
        for ob in Part1:
            i += 1
            Part2.append(rab(ob.long))
            Part2[i].addel(ob.points)
        # ВЫШЕ ПЕРЕВОД ИЗ 1ГО МАССИВА ВО 2Й
        Part2[1].pri()
        f.close()
    except :
        # QMessageBox.about(QtWidgets.QWidget,"Title", "Message")
        # file_bag()
        IsParse = False
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.setWindowTitle("Информация")
        msg.setText("Выбран неверный формат файла, или файл не соответствует входному формату. Пожалуйста, выберите другой файл.")

        okButton = msg.addButton('Окей', QtWidgets.QMessageBox.AcceptRole)
        msg.addButton('Отмена', QtWidgets.QMessageBox.RejectRole)

        msg.exec()


def IsP():
    return (IsParse)